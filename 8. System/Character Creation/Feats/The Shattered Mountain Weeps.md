---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Earth]]", "[[Impulse]]", "[[Kineticist]]", "[[Overflow]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

A massive sphere of rock explodes, unleashing a cataclysm of falling debris and deadly shrapnel. Its destruction falls in a @Template[burst|distance:20] within 120 feet. Creatures in the area take @Damage[(ternary(gte(@actor.level,20),10,9))d10[bludgeoning]|options:area-damage] damage with a [[Fortitude]] save against your class DC. Those who fail are knocked [[Prone]]. For the next minute, rocks continue to fall, making the area difficult terrain and dealing @Damage[(ternary(gte(@actor.level,20),4,3))d10[bludgeoning]|options:area-damage] damage to any creature that ends its turn in the area. If you use this impulse again, any previous one ends.

**Level (20th)** The initial damage is 10d10, and the area damage is 4d10.

**Source:** `= this.source` (`= this.source-type`)
