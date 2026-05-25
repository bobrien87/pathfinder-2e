---
type: action
source-type: "Remaster"
traits: ["[[Gunslinger]]"]
cast: "`pf2:0`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You roll initiative.

You posture defensively with firearms or crossbows, acting like a walking tower. Interact to draw a firearm or crossbow. You then position that weapon defensively, as the parry trait, gaining a +1 circumstance bonus to AC until the end of your first turn, or a +2 circumstance bonus if the chosen weapon has the parry trait.

**Source:** `= this.source` (`= this.source-type`)
