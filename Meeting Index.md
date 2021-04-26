### All OGM Calls by Date (newest first):

```dataview
table
meeting-series as "Meeting Series",
file.size as "File Size"
from "Meetings"
where contains(file.name, "OGM")
sort date desc
```


Note: Show the file in Preview mode to see the list. If you are not seeing the list, please install the community plugin called "Data View", enable the plugin, and re-open the vault.