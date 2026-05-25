---
type: action
source-type: "Remaster"
traits: ["[[Commander]]", "[[Tactic]]"]
cast: "`pf2:2`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Your team works together to set an enemy up for a vicious attack. Signal one squadmate who has an opponent within their reach. That ally can [[Shove]] or [[Reposition]] an opponent as a free action. If their maneuver is successful and the target ends their movement adjacent to a different squadmate, the second squadmate can attempt a melee Strike against that target as a reaction.

**Source:** `= this.source` (`= this.source-type`)
