---
type: heritage
source-type: "Remaster"
ancestry: "Versatile"
traits: ["[[Dromaar]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Orcish strength emboldens your bloodline. You have a green tinge to your skin and other indicators of orc heritage. You gain the orc trait, the dromaar trait, and low-light vision. When you gain an ancestry feat, you can choose from dromaar and orc feats in addition to those from your ancestry.

**Source:** `= this.source` (`= this.source-type`)
