# Meeting Index

## About This Page

This page is used to automatically show indexes of all the Meeting pages in the wiki.

To make it work, it uses the [[YAML Front Matter]] in the wiki pages, and a plugin for Obsidian called "Dataview".  Only the notes with `category` set to "Meeting" will show up here.

In Obsidian, view the page in **Preview** mode to see the indexes. If you are not seeing the indexes, please install the community plugin called "Dataview", enable the plugin, and re-open the vault.

If you see text like `dataview table rows.date` etc., your Massive Wiki viewer does not yet support the Dataview plugin.

## Meetings by Date (newest first)

```dataview
table
rows.date as "Date",
rows.meeting-series as "Meeting Series",
rows.file.link as "Meeting Notes",
rows.recording-video as "Video Link",
rows.file.size as "File Size"
where category = "Meeting"
sort date desc
group by file.path
```


## Meetings by Series (alpha) then Date (newest first)

```dataview
table
rows.meeting-series as "Meeting Series",
rows.date as "Date",
rows.file.link as "Meeting Notes",
rows.recording-video as "Video Link",
rows.file.size as "File Size"
where category = "Meeting"
sort meeting-series asc, date desc
group by file.path
```

