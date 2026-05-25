---
type: class
source-type: "Remaster"
key-attribute: "Int"
hp: "6"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`
**Key Attribute** `= this.key-attribute`; **HP per Level** `= this.hp`

*You command powerful magic, not through study or devotion, but as an agent for an otherworldly patron that even you don't entirely understand. This entity might be a covert divinity, a powerful fey, an ancient spirit, or any other mighty supernatural being—but its nature is likely as much a mystery to you as it is to others. Through a special familiar, your patron grants you versatile spells and powerful hexes to use as you see fit, though you're never certain if you're merely serving your patron's larger plan.*

*Witch*

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
