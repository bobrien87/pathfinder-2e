---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Tanuki|Tanuki]]"
traits: ["[[Tanuki]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your pride in your true tanuki form knows no bounds. You gain your choice of [[Everyday Form]] or [[Teakettle Form]] as a bonus ancestry feat.

**Source:** `= this.source` (`= this.source-type`)
