---
type: action
source-type: "Remaster"
traits: ["[[Commander]]", "[[Tactic]]"]
cast: "`pf2:1`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You command your allies to regroup, allowing endangered units to fall back while rested units press the advantage. Signal all squadmates within the aura of your commander's banner; each can swap positions with another willing ally adjacent to them. An ally can't swap into a space it can't fit into, and if one of the allies occupies more squares than the other, the smaller ally can move into any part of the larger ally's space as long as the two remain adjacent after the swap.

*PFS Note:* This tactic can be used by [[Prone]] PCs, but not PCs who are [[Grabbed]], [[Immobilized]], or otherwise unable to move of their own volition.

**Source:** `= this.source` (`= this.source-type`)
