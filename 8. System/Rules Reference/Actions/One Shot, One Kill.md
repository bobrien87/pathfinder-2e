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

**Trigger** You roll Stealth for initiative.

Your first shot is the deadliest. Interact to draw a firearm or crossbow. Your first successful Strike with that weapon during this encounter deals an additional 1d6 precision damage. This precision damage increases to 2d6 at 9th level and 3d6 at 15th level.

**Source:** `= this.source` (`= this.source-type`)
