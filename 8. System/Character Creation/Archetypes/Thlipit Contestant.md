---
type: archetype
source-type: "Remaster"
prerequisites: "You have a long prehensile tongue or a tail. At the GM's discretion, similar flexible appendages, such as tentacles, can be used to qualify instead."
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "")`

This archetype represents the Thlipit Contestant path. You gain access to its archetype dedication and subsequent feats.

#### Feats
``` dataview
LIST level
WHERE archetype = this.file.link AND lower(type) = "feat"
```

**Source:** `= this.source` (`= this.source-type`)
