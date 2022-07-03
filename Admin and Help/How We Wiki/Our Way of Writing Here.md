# Our Way of Writing Here

Here we describe some of the syntax / semantics / our way of writing on this wiki website.

## Questions

(See "Making Pages" below for these questions)
- When / why / how to write in an existing file?
- When / why / how to create new files?
- When and how do we use folders in this wiki?
- When and how do we use tags (aka #hashtag )

## Wiki Concepts

- also see WikiWay, WikiNature
- [[Chunking]], [[Naming]], [[Linking]]

## Sociology

We'll evolve how we write together.  Some starting thoughts:

- We write in third person, and we don't generally attribute text to any one person.
- Sometimes, we need to write from a single individual's point of view; generally, if you really need to, use a self-pronoun like "my", but add your name in parentheses after, or name yourself in third person (and then someone else might and "and Their Name"). (Pete thinks principle is a good idea.) (It's based on my (Pete) experience with Socialtext and other wikis.)

## Page Maturity

Wiki pages have a life cycle.  Pete has used tree life cycle names, with a page describing each: seed, sprout, seedling, sapling, adult, elderly, snag or rotting log.

How do we want to signal page maturity?  The tree life cycle, or something else?  Use those in tags, or in YAML frontmatter? Etc.

## Making Pages

Make the first line of each page the same as the page filename, as a level 1 header.  (So for example, the first line of this page is `# Our Way of Writing Here`.) This is not strictly necessary in Obsidian, but it helps some of the other clients.

Note that Obsidian won't let you use certain characters in the page filename, because it will cause problems with the filesystem. So, don't use those characters in either the page filename or the first line of the page.

Pages can be a short chapter, or a concept. Basically, a place you'd want to land on from a link. 

Conversely, pages generally shouldn't end up super short; a page should have a couple of paragraphs at least, when it gets fully developed.

It's okay to have very little in a page when it gets started, of course.

## Some Simple Markdown Rules

- Generally, use the dash character for bullet lists rather than asterisks. (Either works, but in a few cases, the dash is better for obscure reasons.)
- Similarly, you can use either underscore or asterisk for italic and bold; prefer underscore for italic, and asterisk for bold: `_italic_` and `**bold**`.
- Different editors need or don't need an empty/blank line between different kinds of elements, such as headers and bullet lists.  In general, you should use a blank line between different kinds of elements, to be most generally compatible.

## More Advanced Markdown

To make a link to a page but have different text show in the link, use a vertical bar character.  For instance, `[[Peter Kaminski|Pete]]` produces [[Peter Kaminski|Pete]].  And `[[Choice|Choices]]` makes [[Choice|Choices]].

To make it so wikitext is displayed verbatim (rather than being parsed), in a monospaced font, enclose the wikitext in a pair of backticks.

If you want multiple lines not parsed and in monospaced font, use three backticks on one line above your lines, and three backticks on the line after your lines.

(add something here about double space characters for linebreaks, used on sidebars)

### Misc. Notes
- Incipient Links - links to things that don't exist yet... are just as important as a page. You can make them, without stopping your train of thought, and they will be there as placeholders. 
	- Obsidian knows a link that doesn't exist is still a link. 
	- If you click on the [[Incipient Link]], then the page exists. 
- Hashtags - #hashtag - 
- Over time, we need to evolve towards both the right kinds of hierarchy and linking, and have wiki gardeners develop guidance nodes, jump pages, and other tools. 
- Table of contents page, maps of content, and jump pages are similar. 
