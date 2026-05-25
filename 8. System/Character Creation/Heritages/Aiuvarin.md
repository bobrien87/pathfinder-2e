---
type: heritage
source-type: "Remaster"
ancestry: "Versatile"
traits: ["[[Aiuvarin]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You have elves, or possibly other aiuvarins, in your family tree. You have pointed ears and other telltale signs of elf heritage. You gain the elf trait, the aiuvarin trait, and low-light vision. In addition, when you gain an ancestry feat, you can choose from aiuvarin and elf feats in addition to those from your ancestry.

**Source:** `= this.source` (`= this.source-type`)
