---
type: archetype
source-type: "Remaster"
prerequisites: "Familiar Master Dedication, you have befriended a spirit guide and it bonded with you using its Bond with Mortal ability."
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "")`

This archetype represents the Scions Of Domora path. You gain access to its archetype dedication and subsequent feats.

#### Feats
``` dataview
LIST level
WHERE archetype = this.file.link AND lower(type) = "feat"
```

**Source:** `= this.source` (`= this.source-type`)
