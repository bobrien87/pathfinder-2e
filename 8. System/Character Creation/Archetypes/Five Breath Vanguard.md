---
type: archetype
source-type: "Remaster"
prerequisites: "Two of the five elemental stances (Ironblood Stance, Mountain Stance, Reflective Ripple Stance, Stoked Flame Stance, and Tangled Forest Stance)"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "")`

This archetype represents the Five Breath Vanguard path. You gain access to its archetype dedication and subsequent feats.

#### Feats
``` dataview
LIST level
WHERE archetype = this.file.link AND lower(type) = "feat"
```

**Source:** `= this.source` (`= this.source-type`)
