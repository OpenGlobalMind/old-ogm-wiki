# Ideas Dashboard

In Obsidian, view this page in **Preview** mode to see the dashboard. If you are not seeing the dashboard in preview mode, please install the community plugin called "Dataview", enable the plugin, and re-open the vault.

If you see text like `dataview table rows.file.link` etc., your Massive Wiki viewer does not yet support the Dataview plugin.

```dataview
table
rows.file.link as "Idea",
rows.shepherd as "Shepherd"
where category = "Idea"
group by file.name
```
