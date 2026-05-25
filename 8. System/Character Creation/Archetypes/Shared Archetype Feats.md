---
type: archetype
source-type: "Remaster"
prerequisites: "Acrobat, Celebrity, Dandy, or Gladiator Dedication, Quick Disguise, master in Deception"
source: "Pathfinder #204: Stage Fright"
---
### `= this.file.name`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "")`

This archetype represents the Shared Archetype Feats path. You gain access to its archetype dedication and subsequent feats.

#### Feats
``` dataview
LIST level
WHERE archetype = this.file.link AND lower(type) = "feat"
```

**Source:** `= this.source` (`= this.source-type`)
