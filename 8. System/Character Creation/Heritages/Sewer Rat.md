---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Ratfolk|Ratfolk]]"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

You come from a long line of ratfolk with a community based in the sewers beneath a large settlement. You are immune to the disease putrid plague. You gain a +1 circumstance bonus to saving throws against diseases and poisons. If you roll a success on a saving throw against a disease or poison, you get a critical success instead. If you have a different ability that would improve the save in this way (such as the [[Battle Hardened]] fighter class feature), if you roll a critical failure on the save you get a failure instead.

**Source:** `= this.source` (`= this.source-type`)
