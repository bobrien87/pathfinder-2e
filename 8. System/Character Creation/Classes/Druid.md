---
type: class
source-type: "Remaster"
key-attribute: "Wis"
hp: "8"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`
**Key Attribute** `= this.key-attribute`; **HP per Level** `= this.hp`

*The power of nature is impossible to resist. It can bring ruin to the stoutest fortress in minutes, reducing even the mightiest works to rubble, burning them to ash, burying them beneath an avalanche of snow, or drowning them beneath the waves. It can provide endless bounty and breathtaking splendor to those who respect it—and an agonizing death to those who take it too lightly. You are one of those who hear nature's call. You stand in awe of the majesty of its power and give yourself over to its service.*

Druid

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
