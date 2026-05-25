---
type: action
source-type: "Remaster"
traits: ["[[Gunslinger]]"]
cast: "`pf2:1`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

As you sink deep into a state of analytical calm and focus on the foe before you, your hands reload a bullet instinctively. Attempt a Recall Knowledge check against an opponent you can see and then Interact to reload.

**Source:** `= this.source` (`= this.source-type`)
