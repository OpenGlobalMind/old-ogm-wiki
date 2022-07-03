# -*- coding: utf-8 -*-
'''
Massive Wiki Builder WikiLinkPlus Extension for Python-Markdown
===========================================

Converts [[WikiLinks]] to relative links.
Based on <https://github.com/neurobin/mdx_wikilink_plus>
See <https://github.com/neurobin/mdx_wikilink_plus> for mdx_wikilink_plus documentation.
Copyright Md. Jahidul Hamid <jahidulhamid@yahoo.com>
License: [BSD](http://www.opensource.org/licenses/bsd-license.php)

Modifications to create mwb_wikilink_plus.py
Copyright William L. Anderson <band@acm.org> and Peter Kaminski <kaminski@istori.com>
License: [BSD](http://www.opensource.org/licenses/bsd-license.php)
'''

from __future__ import absolute_import
from __future__ import unicode_literals
try:
    from urllib.parse import urlparse
    from urllib.parse import urlunparse
except ImportError:
    from urlparse import urlparse
    from urlparse import urlunparse
import markdown
from markdown.util import etree
import re
import os
from . import version

__version__ = version.__version__

MARKDOWN_MAJOR = markdown.version_info[0]

WIKILINK_PLUS_RE = r'\[\[\s*(?P<target>[^][|]+?)(\s*\|\s*(?P<label>[^][]+))?\s*\]\]'

def build_url(urlo, base, end, url_whitespace, url_case):
    """ Build and return a valid url.

    Parameters
    ----------

    urlo            A ParseResult object returned by urlparse

    base            base_url from config

    end             end_url from config

    url_whitespace  url_whitespace from config

    url_case        url_case from config

    Returns
    -------

    URL string

    """
    if not urlo.netloc:
        if not end:
            clean_target = re.sub(r'\s+', url_whitespace, urlo.path)
        else:
            clean_target = re.sub(r'\s+', url_whitespace, urlo.path.rstrip('/'))
            if clean_target.endswith(end):
                end = ''
        if base.endswith('/'):
            path = "%s%s%s" % (base, clean_target.lstrip('/'), end)
        elif base and not clean_target.startswith('/'):
            path = "%s/%s%s" % (base, clean_target, end)
        else:
            path = "%s%s%s" % (base, clean_target, end)
        if url_case == 'lowercase':
            urlo = urlo._replace(path=path.lower() )
        elif url_case == 'uppercase':
            urlo = urlo._replace(path=path.upper() )
        else:
            urlo = urlo._replace(path=path)
    return urlunparse(urlo)


def title(subject):
    """Return title cased version of the given subject string"""
    exceptions = ['a', 'an', 'the', 'v', 'vs', 'am', 'at', 'and', 'as', 'but','by', 'en', 'for', 'if', 'be', 'in', 'of', 'on', 'or', 'to', 'via',]
    slst = list(filter(None, re.split(r'[ \t]+', subject)))
    res = []
    c = 0
    for s in slst:
        if re.match(r'^[^a-z]+$', s) or (s in exceptions and c != 0):
            res.append(s)
        else:
            res.append(s.title())
        c = c + 1
    return ' '.join(res)

class WikiLinkPlusExtension(markdown.Extension):
    """WikiLinkPlus Extension class for markdown"""

    def __init__(self,  configs={}):
        self.config = {
            'base_url': ['', 'String to append to beginning or URL.'],
            'end_url': ['', 'String to append to end of URL.'],
            'url_whitespace': ['-', 'String to replace white space in the URL'],
            'label_case':['titlecase', "Other valid values are: capitalize and none"],
            'url_case':['none', "Other valid values are: lowercase and uppercase"],
            'html_class': ['wikilink', 'CSS hook. Leave blank for none.'],
            'image_class': ['wikilink-image', 'CSS hook. Leave blank for none.'],
            'build_url': [build_url, 'Callable formats URL from label.'],
        }
        for k, v in configs.items():
            self.setConfig(k, v)

    def extendMarkdown(self, *args):
        md = args[0]
        self.md = md

        # append to end of inline patterns
        ext = WikiLinkPlusPattern(self.config, md)
        if MARKDOWN_MAJOR == 2:
            md.inlinePatterns.add('wikilink_plus', ext, "<not_strong")
        else:
            md.inlinePatterns.register(ext, 'wikilink_plus', 76)


class WikiLinkPlusPattern(markdown.inlinepatterns.Pattern):
    def __init__(self, config, md=None):
        markdown.inlinepatterns.Pattern.__init__(self, '', md)
        self.compiled_re = re.compile("^(.*?)%s(.*?)$" % (WIKILINK_PLUS_RE,), re.DOTALL | re.X)
        self.config = config
        self.md = md

    def getCompiledRegExp(self):
        return self.compiled_re

    def handleMatch(self, m):
        """Return an a element if regex matched"""
        d = m.groupdict()
        tl = d.get('target')
        label = d.get('label')
        if label is None:
            label = tl
        if tl:
            base_url, end_url, url_whitespace, url_case, label_case, html_class, image_class = self._getMeta()
            clean_path = tl
            isimage = False
            imagesuffixes = ['.png', '.jpg', '.jpeg', '.gif', '.svg']
            for suffix in imagesuffixes:
                if clean_path.lower().endswith(suffix):
                    isimage = True
                    break
            if not isimage:
                url = self.config['build_url'][0](clean_path, base_url, end_url, url_whitespace, url_case)
                a = etree.Element('a')
                a.text = label
                a.set('href', url)
                if html_class:
                    a.set('class', html_class)
            else:
                end_url = ''
                url = self.config['build_url'][0](clean_path, base_url, end_url, url_whitespace, url_case)
                a = etree.Element('img')
                pipes = label.split('|')
                for pipe in pipes:
                    option = [option.strip() for option in pipe.split('=')]
                    if option[0] == 'alt':
                        a.set('alt', option[1])
                        break
                a.set('src', url)
                if image_class:
                    a.set('class', image_class)
        else:
            a = ''
        return a

    def _getMeta(self):
        """ Return meta data or config data. """
        base_url = self.config['base_url'][0]
        end_url = self.config['end_url'][0]
        url_whitespace = self.config['url_whitespace'][0]
        label_case = self.config['label_case'][0]
        url_case = self.config['url_case'][0]
        html_class = self.config['html_class'][0]
        image_class = self.config['image_class'][0]
        if hasattr(self.md, 'Meta'):
            if 'wiki_base_url' in self.md.Meta:
                base_url = self.md.Meta['wiki_base_url'][0]
            if 'wiki_end_url' in self.md.Meta:
                end_url = self.md.Meta['wiki_end_url'][0]
            if 'wiki_url_whitespace' in self.md.Meta:
                url_whitespace = self.md.Meta['wiki_url_whitespace'][0]
            if 'wiki_label_case' in self.md.Meta:
                label_case = self.md.Meta['wiki_label_case'][0]
            if 'wiki_url_case' in self.md.Meta:
                url_case = self.md.Meta['wiki_url_case'][0]
            if 'wiki_html_class' in self.md.Meta:
                html_class = self.md.Meta['wiki_html_class'][0]
            if 'wiki_image_class' in self.md.Meta:
                image_class = self.md.Meta['wiki_image_class'][0]
        return base_url, end_url, url_whitespace, url_case, label_case, html_class, image_class


def makeExtension(*args, **kwargs):  # pragma: no cover
    return WikiLinkPlusExtension(kwargs)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
