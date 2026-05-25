---
type: class
source-type: "Remaster"
key-attribute: "Dex"
hp: "8"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`
**Key Attribute** `= this.key-attribute`; **HP per Level** `= this.hp`

*You are skilled and opportunistic. Using your sharp wits and quick reactions, you take advantage of your opponents' missteps and strike where it hurts most. You play a dangerous game, seeking thrills and testing your skills, and likely don't care much for any laws that happen to get in your way. While the path of every rogue is unique and riddled with danger, the one thing you all share in common is the breadth and depth of your skills.*

*Rogue*

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
