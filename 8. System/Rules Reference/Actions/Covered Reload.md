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

You duck into a safe position or minimize your profile while reloading to make your next attack. Either [[Take Cover]] or attempt to [[Hide]], then Interact to reload. As normal, you must meet the requirements to Take Cover or Hide; you must be [[Prone]], benefiting from cover, or near a feature that allows you to Take Cover, and you need to be benefiting from cover or [[Concealed]] to a creature to Hide from that creature.

**Source:** `= this.source` (`= this.source-type`)
