---
type: class
source-type: "Remaster"
hp: "6"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`
**Key Attribute** `= this.key-attribute`; **HP per Level** `= this.hp`

*The mind can perceive truths hidden to fine-tuned instruments, house more secrets than any tome, and move objects and hearts more deftly than any lever. By delving into both the conscious and subconscious aspects of your inner self, you have awoken to the might of psychic magic, allowing you to cast spells not through incantations or gestures but by the power of your will alone. While the thin line between your mind and reality means that a single errant thought could have unintended consequences for yourself and your companions, you know that anything is possible, if you can imagine it.*

*Psychic*

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
