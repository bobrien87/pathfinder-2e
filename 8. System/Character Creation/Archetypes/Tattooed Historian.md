---
type: archetype
source-type: "Remaster"
prerequisites: "Constitution +1, trained in Belkzen Lore, Orc Lore, Orc Pantheon Lore, or (at the GM's discretion) a related Lore skill"
source: "Pathfinder #207: The Resurrection Flood"
---
### `= this.file.name`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "")`

This archetype represents the Tattooed Historian path. You gain access to its archetype dedication and subsequent feats.

#### Feats
``` dataview
LIST level
WHERE archetype = this.file.link AND lower(type) = "feat"
```

**Source:** `= this.source` (`= this.source-type`)
