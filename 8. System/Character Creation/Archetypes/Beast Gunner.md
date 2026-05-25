---
type: archetype
source-type: "Remaster"
prerequisites: "expert with at least one type of firearm, trained in Arcana or Crafting, you own a beast gun and have slain the type of creature associated with your beast gun in a fair hunt"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "")`

This archetype represents the Beast Gunner path. You gain access to its archetype dedication and subsequent feats.

#### Feats
``` dataview
LIST level
WHERE archetype = this.file.link AND lower(type) = "feat"
```

**Source:** `= this.source` (`= this.source-type`)
