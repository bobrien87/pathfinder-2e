---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Halfling|Halfling]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You hail from deep within a jungle or forest, and you've learned how to use your small size to wriggle through undergrowth and other obstacles. You ignore any difficult terrain caused by plants and fungi, such as bushes, vines, and undergrowth.

**Source:** `= this.source` (`= this.source-type`)
