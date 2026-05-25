---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Overflow]]", "[[Primal]]", "[[Wood]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

A fusillade of jagged splinters flies from you. Creatures in a @Template[cone|distance:30] take @Damage[(floor((@actor.level -1)/2)+1)d4[piercing],(floor((@actor.level -1)/2)+1)d4[persistent,bleed]|options:area-damage] damage with a [[Reflex]] save against your class DC.

**Level (+2)** Each type of damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
