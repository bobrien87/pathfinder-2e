---
type: archetype
source-type: "Remaster"
prerequisites: "expert in Stealth, expert in Survival, member of the Bellflower Network, Charisma +2"
access: ""
source: "Pathfinder #147: Tomorrow Must Burn"
---
### `= this.file.name`
`= choice(this.prerequisites != null, "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null, choice(this.prerequisites != null, "<br>", "") + "**Access** " + this.access, "")`

This archetype represents the Level 6 path. You gain access to its archetype dedication and subsequent feats.

#### Feats
``` dataview
LIST level
WHERE archetype = this.file.link AND lower(type) = "feat"
```

**Source:** `= this.source` (`= this.source-type`)
