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

You know trouble can lurk around every corner, and your hands never stray far from your holsters. You can Interact to draw a one-handed ranged weapon and can then Interact to draw a one-handed melee weapon. As your first action on your first turn, you can Stride as a free action toward an enemy you can perceive. If you can't perceive any enemies or can't end your movement closer to one, you can't use this Stride.

**Source:** `= this.source` (`= this.source-type`)
