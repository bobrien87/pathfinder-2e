---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Overflow]]", "[[Plant]]", "[[Polymorph]]", "[[Primal]]", "[[Wood]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You touch a creature to implant a malignant seed in its body. The creature takes @Damage[(floor((@actor.level -12)/4)+5)d10[piercing]] damage and other effects depending on its [[Fortitude]] save against your class DC. The creature is then temporarily immune for 24 hours. Creatures with the fungus, plant, or wood trait are immune.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage and takes a –10-foot status penalty to all its Speeds until the end of its next turn.
- **Failure** The target takes full damage and is [[Clumsy]] 2 and [[Immobilized]] until the end of its next turn.
- **Critical Failure** The target takes double damage and is clumsy 2 and immobilized. It attempts a new save at the end of each of its turns, ending the effect if it succeeds.

**Level (+4)** The damage increases by 1d10.

**Source:** `= this.source` (`= this.source-type`)
