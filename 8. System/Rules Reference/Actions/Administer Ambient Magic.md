---
type: action
source-type: "Remaster"
traits: ["[[Healing]]"]
cast: "`pf2:1`"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per hour

**Effect** Your ostilli pulses a calm lavender color as it converts stored magic into a curative balm. You regain @Damage[((2*floor(@actor.level/4))d4)[healing]] Hit Points, and you can immediately attempt a flat check to recover from persistent bleed damage with the DC reduced to 10. This healing increases by 2d4 at 8th level and every 4 levels thereafter.

**Source:** `= this.source` (`= this.source-type`)
