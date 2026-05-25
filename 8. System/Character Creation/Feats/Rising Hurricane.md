---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Air]]", "[[Composite]]", "[[Impulse]]", "[[Kineticist]]", "[[Overflow]]", "[[Primal]]", "[[Water]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

A hurricane lifts your enemies into the air before bringing them crashing down in a bloody rain. Your hurricane appears in a cylinder that's 40 feet tall, has a @Template[cylinder|distance:15]{30-foot diameter}, and is within 120 feet. All creatures in the area take @Damage[(floor((@actor.level -6)/3)+2)d6[bludgeoning]|options:area-damage] damage with a [[Fortitude]] save against your class DC. Lift any creature that fails its save to any height you choose within the area, move it up to 5 feet in any direction, then drop it. It takes falling damage normally unless it has a fly Speed.

**Level (+3)** The rain damage increases by 1d6, and the cylinder's height increases by 5 feet.

**Source:** `= this.source` (`= this.source-type`)
