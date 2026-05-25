---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Overflow]]", "[[Plant]]", "[[Primal]]", "[[Wood]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Blood-drinking vines grow from the ground in a @Template[burst|distance:15] within 120 feet. Each living enemy in the area has its blood drained, taking @Damage[(floor((@actor.level -8)/2)+3)d6[piercing]|options:area-damage] damage with a [[Fortitude]] save against your class DC. Each time the vines drink blood, living creatures in the area who aren't your enemies regain HP equal to half the damage a single creature took; calculate this using the highest damage a single creature took. This is a healing vitality effect. Your enemies with void healing in the area take vitality damage in the same amount as the healing.

The vines last until the end of your next turn, and you can Sustain the impulse. The first time you Sustain the impulse on subsequent turns, you can repeat the effect.

**Level (+2)** The damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
