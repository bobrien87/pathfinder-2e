---
type: archetype
source-type: "Remaster"
prerequisites: "Wisdom +2"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "")`

This archetype represents the Druid path. You gain access to its archetype dedication and subsequent feats.

#### Feats
``` dataview
LIST level
WHERE archetype = this.file.link AND lower(type) = "feat"
```

**Source:** `= this.source` (`= this.source-type`)
