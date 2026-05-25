---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Composite]]", "[[Earth]]", "[[Fire]]", "[[Impulse]]", "[[Kineticist]]", "[[Overflow]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You wreath yourself in molten stone and hurtle toward your enemy. [[Leap]] up to your Speed. At the end of your Leap, a wave of lava crashes onto all creatures in a @Template[emanation|distance:10]. Each creature in the area takes @Damage[(floor((@actor.level -4)/3)+1)d6[bludgeoning], (floor((@actor.level -4)/3)+2)d6[fire]|options:area-damage] damage, with a [[Reflex]] save against your class DC.

The cooling remains of the lava form a temporary protective shell around you, granting you a +2 circumstance bonus to AC until the start of your next turn.

**Level (+3)** Each type of damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
