---
type: heritage
source-type: "Remaster"
ancestry: "Versatile"
traits: ["[[Ardande]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You descend from wood elementals or have some other heritage influenced by the elemental Plane of Wood. You might have green, mossy skin, vines that grow from your head instead of hair, or thin appendages that resemble twigs. You gain the ardande trait, in addition to the traits from your ancestry. You also gain low-light vision, or you gain darkvision if your ancestry already has low-light vision.

You can choose from ardande feats, geniekin feats, and feats from your ancestry whenever you gain an ancestry feat.

**Source:** `= this.source` (`= this.source-type`)
