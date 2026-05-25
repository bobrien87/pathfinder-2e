---
type: heritage
source-type: "Remaster"
ancestry: "Versatile"
traits: ["[[Changeling]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your mother was a hag. Your eyes' heterochromia is the most obvious signifier of this parentage, but you likely also have a slighter build, paler skin, and darker hair than most members of your other parent's ancestry. You gain the changeling trait. You also gain low-light vision, or you gain darkvision if your ancestry already has low-light vision. You can select from changeling feats and feats from your other parent's ancestry whenever you gain an ancestry feat.

**Source:** `= this.source` (`= this.source-type`)
