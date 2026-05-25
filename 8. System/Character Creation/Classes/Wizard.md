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

*You are an eternal student of the secrets of the universe, using your mastery of magic to cast powerful spells. You treat magic like a science, cross-referencing the latest texts on practical spellcraft with ancient tomes to discover and understand arcane magic. Yet magical theory is vast, and there's no way you can study it all. Most wizards learn through formal schooling, with their curriculum informing a specific rubric, although particularly driven researchers sometimes piece together their own theories.*

*Wizard*

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
