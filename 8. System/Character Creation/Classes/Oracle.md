---
type: class
source-type: "Remaster"
key-attribute: "Cha"
hp: "8"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`
**Key Attribute** `= this.key-attribute`; **HP per Level** `= this.hp`

*Your conduit to divine power eschews the traditional channels of prayer and servitude—you instead glean sacred truths and great mysteries embodied in overarching concepts, whether because you perceive the common ground across multiple deities or circumvent their power entirely.*

*You explore one of these mysteries and draw upon its power to cast miraculous spells, but that power comes with a terrible price: a curse that grows stronger the more you draw upon it, which you might uphold as an instrument of the divine or view as punishment from the gods.*

*Oracle*

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
