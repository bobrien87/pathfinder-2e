---
type: action
source-type: "Remaster"
traits: ["[[Auditory]]", "[[Concentrate]]"]
cast: "`pf2:1`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You instruct your construct companion to act as you instruct it, and according to its programming. Your construct companion gains 2 actions during this turn. See the minion trait for details.

**Source:** `= this.source` (`= this.source-type`)
