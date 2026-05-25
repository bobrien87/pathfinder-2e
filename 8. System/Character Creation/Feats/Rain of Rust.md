---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Composite]]", "[[Impulse]]", "[[Kineticist]]", "[[Metal]]", "[[Primal]]", "[[Water]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You conjure a red raincloud in a @Template[burst|distance:10] within 60 feet, which pours rust-colored rain directly below it. Any creature in the rain with the metal trait, that is made of metal, or is wearing metal armor is covered in corrosive build-up. Any such creature is [[Clumsy]] 1 as long as it remains in the area. If such a creature is in the rain at the start of its turn, it takes @Damage[(floor((@actor.level -4)/2)+3)d6[untyped]|options:area-damage] damage with a [[Fortitude]] save against your class DC, plus @Damage[1d6[persistent,untyped]|options:area-damage] damage if it fails. Damage from this impulse ignores Hardness. The cloud lasts 1 minute but ends if you use the impulse again.

**Level (+2)** The initial damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
