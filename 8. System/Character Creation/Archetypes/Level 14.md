---
type: archetype
source-type: "Remaster"
prerequisites: "Incredible Mount"
access: ""
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.prerequisites != null, "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null, choice(this.prerequisites != null, "<br>", "") + "**Access** " + this.access, "")`

This archetype represents the Level 14 path. You gain access to its archetype dedication and subsequent feats.

#### Feats
``` dataview
LIST level
WHERE archetype = this.file.link AND lower(type) = "feat"
```

**Source:** `= this.source` (`= this.source-type`)
