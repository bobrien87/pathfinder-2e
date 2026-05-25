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

You react to trouble with lightning speed, positioning yourself just right. You gain a +2 circumstance bonus to your initiative roll, and you can Interact to draw a one-handed firearm or one-handed crossbow. As your first action on your first turn, you can Step up to 10 feet as a free action.

**Source:** `= this.source` (`= this.source-type`)
