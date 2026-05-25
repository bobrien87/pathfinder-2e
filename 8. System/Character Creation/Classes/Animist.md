---
type: class
source-type: "Remaster"
key-attribute: "Wis"
hp: "8"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`
**Key Attribute** `= this.key-attribute`; **HP per Level** `= this.hp`

*You are the interlocutor between the seen and unseen, the voice that connects the mortal and the spiritual. You bond with spirits, manifesting their distinct magic and allowing their knowledge to flow through you. You may favor apparitions that grant you healing magic, others that grant you spells of destructive power, or pick and choose between different apparitions as your environment and circumstances demand. You may consider your powers part of a sacred trust or see your unique abilities as a sign that you've been chosen as a champion of two worlds. Whether you advocate for mortals in the planes beyond or whether you represent the spirits' interests, you provide the bridge between realms.*

Animist

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
