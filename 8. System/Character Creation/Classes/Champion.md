---
type: class
source-type: "Remaster"
key-attribute: "Dex or Str"
hp: "10"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`
**Key Attribute** `= this.key-attribute`; **HP per Level** `= this.hp`

*You are an emissary of a deity, a devoted servant who has taken up a weighty mantle, and you adhere to a code that holds you apart from those around you. While champions exist for every alignment, as a champion of good, you provide certainty and hope to the innocent. You have powerful defenses that you share freely with your allies and innocent bystanders, as well as holy power you use to end the threat of evil. Your devotion even attracts the attention of holy spirits who aid you on your journey.*

*Champion*

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
