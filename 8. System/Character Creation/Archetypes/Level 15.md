---
type: archetype
source-type: "Remaster"
prerequisites: "Captain Dedication, legendary in Diplomacy or Intimidation"
access: ""
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.prerequisites != null, "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null, choice(this.prerequisites != null, "<br>", "") + "**Access** " + this.access, "")`

This archetype represents the Level 15 path. You gain access to its archetype dedication and subsequent feats.

#### Feats
``` dataview
LIST level
WHERE archetype = this.file.link AND lower(type) = "feat"
```

**Source:** `= this.source` (`= this.source-type`)
