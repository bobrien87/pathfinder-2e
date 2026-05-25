---
type: heritage
source-type: "Remaster"
ancestry: "Versatile"
traits: ["[[Nephilim]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your nature is influenced by celestials, fiends, or monitors. This manifests as a combination of features that belie your heritage, such as golden eyes, a halo, horns, or a tail. You gain the nephilim trait, in addition to the traits from your ancestry. You gain low-light vision, or you gain darkvision if your ancestry already has low-light vision. You can choose from nephilim feats and feats from your ancestry whenever you gain an ancestry feat.

**Source:** `= this.source` (`= this.source-type`)
