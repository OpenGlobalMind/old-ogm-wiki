# How to Get Permalinks for Obsidian Pages
Per [[Peter Kaminski]]: 

Note that there are two permalinks, one to GitHub, and one to `[wiki.openglobalmind.com](http://wiki.openglobalmind.com/)`.

Then, actually, there are sort of two at `[wiki.openglobalmind.com](http://wiki.openglobalmind.com/)`: one to an HTML rendering of it, and one to the Markdown source file.

The short answer is yes, it might be easiest to find it in Github, or on the web version of the wiki.

The longer answer is that you can look up the "prefix" of each permalink to find out what it is; but then the suffix with the filename is deterministically created from the filename in Obsidian. So once you know the prefix and the deterministic rules, you can create additional permalinks for other files by editing a permalink from another file, or by constructing the permalink from the prefix or the rules.

Whether or not that's easier probably depends on your workflow, how often you do it, etc.

So for instance:

-   title: Playing with Excalidraw.excalidraw
-   filename: Playing with [Excalidraw.excalidraw.md](http://excalidraw.excalidraw.md/) (add .md)
-   path + filename: Excalidraw/Playing with [Excalidraw.excalidraw.md](http://excalidraw.excalidraw.md/) (found by inspection, perhaps with "Show in system explorer")
-   GitHub: [https://github.com/OpenGlobalMind/ogm-wiki/blob/main/Excalidraw/The%20View%20from%20Rel8&#39;s%20Mast.excalidraw.md](https://github.com/OpenGlobalMind/ogm-wiki/blob/main/Excalidraw/The%20View%20from%20Rel8&#39;s%20Mast.excalidraw.md)
-   MWB: [https://wiki.openglobalmind.com/excalidraw/playing_with_excalidraw.excalidraw](https://wiki.openglobalmind.com/excalidraw/playing_with_excalidraw.excalidraw) (HTML)
-   MWB: [https://wiki.openglobalmind.com/excalidraw/playing_with_excalidraw.excalidraw.md](https://wiki.openglobalmind.com/excalidraw/playing_with_excalidraw.excalidraw.md) (add .md)
-   Obsidian local URL: obsidian://open?vault=ogm-wiki&file=Excalidraw%2FPlaying%20with%20Excalidraw.excalidraw (filename part perhaps useful to construct GitHub permalink, otherwise not useful except to Obsidian)

The deterministic rules:

For GitHub, take the path + filename, convert space characters to "%20". Prepend "[https://github.com/OpenGlobalMind/ogm-wiki/blob/main/](https://github.com/OpenGlobalMind/ogm-wiki/blob/main/)". (Certain other characters like `#` or `?` may need conversion too, let's ignore that for now.)

For MWB, take the path + filename, make all letters lowercase, convert any run of non-alphanumeric characters to `_`. Prepend "[https://wiki.openglobalmind.com/](https://wiki.openglobalmind.com/)". If you want the Markdown version, append ".md".