---
type: class
source-type: "Remaster"
key-attribute: "Str"
hp: "12"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`
**Key Attribute** `= this.key-attribute`; **HP per Level** `= this.hp`

*Death and danger from all manner of enemies threaten all that you and your companions hold dear. But you are the shield, the steel wall that holds back the tide of opposition. You're clad in armor you wear like a second skin and can angle it to protect yourself and your allies from damage and keep foes at bay. Allies look to you to safeguard them, whether they stand beside you on the battlefield or remain on the back lines, and enemies see you for the imposing threat you are. Be it to friend or foe, your presence is difficult to ignore.*

Guardian

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
