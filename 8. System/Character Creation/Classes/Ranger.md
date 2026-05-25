---
type: class
source-type: "Remaster"
key-attribute: "Dex or Str"
hp: "10"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`
**Key Attribute** `= this.key-attribute`; **HP per Level** `= this.hp`

*Some rangers believe civilization wears down the soul, but still needs to be protected from wild creatures. Others say nature needs to be protected from the greedy, who wish to tame its beauty and plunder its treasures. You could champion either goal, or both. You might be a scout, tracker, or hunter of fugitives or beasts, haunting the edge of civilization or exploring the wilds. You know how to live off the land and are skilled at spotting and taking down both opportune prey and hated enemies.*

*Ranger*

#### Class Features
``` dataview
LIST level
WHERE contains(file.outlinks, this.file.link) AND type = "class-feature"
```

#### Subclasses / Paths
``` dataview
LIST
WHERE contains(file.outlinks, this.file.link) AND type = "subclass"
```

**Source:** `= this.source` (`= this.source-type`)
