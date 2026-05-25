---
type: class
source-type: "Remaster"
key-attribute: "Cha"
hp: "8"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`
**Key Attribute** `= this.key-attribute`; **HP per Level** `= this.hp`

*You are a master of artistry, a scholar of hidden secrets, and a captivating persuader. Using powerful performances, you influence minds and elevate souls to new levels of heroics. You might use your powers to become a charismatic leader, or perhaps you might instead be a counselor, manipulator, scholar, scoundrel, or virtuoso. While your versatility leads some to consider you a beguiling ne'er-do-well and a jack-of-all-trades, it's dangerous to dismiss you as a master of none.*

*Bard*

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
