---
type: class
source-type: "Remaster"
key-attribute: "Int"
hp: "8"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`
**Key Attribute** `= this.key-attribute`; **HP per Level** `= this.hp`

*You seek to uncover the truth, doggedly pursuing leads to reveal the plots of devious villains, discover ancient secrets, or unravel other mysteries. Your analytical mind quickly formulates solutions to complicated problems and your honed senses identify even the most obscure clues. Wielding knowledge as a weapon, you study the creatures and dangers you encounter to exploit their weaknesses.*

*Investigator*

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
