---
type: class
source-type: "Remaster"
key-attribute: "Int"
hp: "8"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`
**Key Attribute** `= this.key-attribute`; **HP per Level** `= this.hp`

*You approach battle with the knowledge that tactics and strategy are every bit as crucial as brute strength or numbers. You might have trained in classical theories of warfare and strategy at a military academy, or you might have refined your techniques through hard-won experience as part of an army or mercenary company. Regardless of how you came by your knowledge, you have a gift for signaling your allies from across the battlefield and deploying commands to rout even the most desperate conflicts, empowering your squad to exceed their limits and claim victory.*

Commander

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
