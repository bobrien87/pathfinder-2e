---
type: class
source-type: "Remaster"
key-attribute: "Dex or Str"
hp: "10"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`
**Key Attribute** `= this.key-attribute`; **HP per Level** `= this.hp`

*As the war god died, his power rained through the many planes of creation, sparking conflict and instilling divine energy in those previously without it. Whether you were directly touched by this power, claimed it from an ancient being or artifact, or whether it awoke something long dormant in your lineage, a spark of the divine now blazes within your soul, granting you abilities, sacred weapons, and divine signifiers that reach into the realm previously reserved for gods and legends. How you wield these tools and grow your power is for you to decide—you may become a hero or you may turn to selfish ends, but one thing is certain: you intend to carve your epithet in history, immortalized in the memory of gods and mortals alike.*

Exemplar

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
