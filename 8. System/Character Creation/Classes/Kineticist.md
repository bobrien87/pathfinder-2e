---
type: class
source-type: "Remaster"
key-attribute: "Con"
hp: "8"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`
**Key Attribute** `= this.key-attribute`; **HP per Level** `= this.hp`

*The power of the elements flows from within you. Roaring fire pure water, fleeting air, steadfast earth, twisting wood, slicing metal. A kinetic gate inextricably tied to your body channels power directly from the elemental planes, causing elements to leap to your hand, whirl around your body, and blast foes at your whim. As your connection to the planes grows, you attain true mastery over your chosen elements.*

*Kineticist*

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
