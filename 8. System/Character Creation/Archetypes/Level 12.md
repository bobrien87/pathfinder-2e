---
type: archetype
source-type: "Remaster"
prerequisites: ""
access: ""
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
`= choice(this.prerequisites != null, "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null, choice(this.prerequisites != null, "<br>", "") + "**Access** " + this.access, "")`

This archetype represents the Level 12 path. You gain access to its archetype dedication and subsequent feats.

#### Feats
``` dataview
LIST level
WHERE archetype = this.file.link AND lower(type) = "feat"
```

**Source:** `= this.source` (`= this.source-type`)
