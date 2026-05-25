---
type: class
source-type: "Remaster"
key-attribute: "Str"
hp: "12"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`
**Key Attribute** `= this.key-attribute`; **HP per Level** `= this.hp`

*Rage consumes you in battle. You delight in wreaking havoc and using powerful weapons to carve through your enemies, relying on astonishing durability without needing complicated techniques or rigid training. Your rages draw upon a vicious instinct, which you might associate with an animal, a spirit, or some part of yourself. To many barbarians, brute force is a hammer and every problem looks like a nail, whereas others try to hold back the storm of emotions inside them and release their rage only when it matters most.*

Barbarian

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
