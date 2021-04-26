### All OGM Calls by Date (newest first):

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


Notes: 
(1) Show the file in **Preview** mode to see the list. If you are not seeing the list, please install the community plugin called "Data View", enable the plugin, and re-open the vault.
(2) only the notes with Category set to "Meeting" will show up here
