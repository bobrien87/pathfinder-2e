---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Earth]]", "[[Impulse]]", "[[Kineticist]]", "[[Overflow]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

A packed cloud of thundering boulders descends from the sky, beating down everyone in its path. The rain of stone falls in a @Template[cylinder|distance:10]{cylinder 20 feet in diameter} and 80 feet high, and the bottom must be within 120 feet of you. Each creature in the area takes @Damage[(floor((@actor.level -6)/2)+4)d8[bludgeoning]|options:area-damage] damage and might be pushed downward, depending on its [[Reflex]] save against your class DC.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage and is pushed downward 40 feet without taking falling damage. If it reaches the bottom of the cylinder or the ground, the push ends. If the creature is pushed to the ground, it can't Fly, [[Levitate]], or otherwise leave the ground for 1 round.
- **Critical Failure** As failure, but double damage and the distance the creature is pushed is 80 feet.

**Level (+2)** The damage increases by 1d8.

**Source:** `= this.source` (`= this.source-type`)
