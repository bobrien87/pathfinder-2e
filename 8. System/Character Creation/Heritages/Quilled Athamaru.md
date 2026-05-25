---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Athamaru|Athamaru]]"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Sharp quills on your head can pierce your foes deeply. Most athamarus use such quills for defense, but a well-timed headbash can be devastatingly effective. You gain a quills melee unarmed attack that deals 1d6 piercing damage. Your quills are in the brawling group and have the agile, finesse, and unarmed traits.

**Source:** `= this.source` (`= this.source-type`)
