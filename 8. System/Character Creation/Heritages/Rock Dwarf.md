---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Dwarf|Dwarf]]"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your ancestors lived and worked among the ancient stones of the mountains or the depths of the earth. This makes you solid as a rock when you plant your feet. You gain a +2 circumstance bonus to your Fortitude or Reflex DC against attempts to [[Reposition]], [[Shove]], or [[Trip]] you. This bonus also applies to saving throws against spells or effects that attempt to force you to move or knock you [[Prone]].

In addition, if any effect would force you to move 10 feet or more, you are moved only half the distance.

**Source:** `= this.source` (`= this.source-type`)
