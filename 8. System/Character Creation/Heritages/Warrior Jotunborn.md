---
type: heritage
source-type: "Remaster"
ancestry: "[[8. System/Character Creation/Ancestries/Jotunborn|Jotunborn]]"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Heritage**
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Ancestry** " + this.ancestry`
`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "")`

Your hardier body made you a perfect recruit for combat. The damage die for your fist increases to 1d6. You don't take a penalty when making a lethal attack with your fist.

**Source:** `= this.source` (`= this.source-type`)
