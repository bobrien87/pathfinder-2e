---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Overflow]]", "[[Primal]]", "[[Wood]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The seasons shift rapidly. This impulse affects a cube 100 feet in each dimension within 1,000 feet. Choose the starting season. The impulse lasts for 4 rounds, proceeding to the next season at the start of each of your turns. You can't use this impulse again until the previous one ends.

**Spring** Each ally in the cube gains 20 temporary HP that last until the start of your next turn. Any dying ally rolls a recovery check, but can't get worse than a success.

**Summer** (light) Each enemy in the area is exposed to sunlight and must attempt a [[Reflex]] save against your class DC. It's unaffected on a critical success, [[Dazzled]] until the start of your next turn on a success, or [[Blinded]] until the start of your next turn on a failure.

**Autumn** Leaves and rain make everything in the area [[Concealed]] until the start of your next turn, and a cold wind makes each enemy in the area [[Slowed]] 1 until the start of your next turn unless it succeeds at a [[Fortitude]] save against your class DC.

**Winter** Each enemy in the aura takes @Damage[5d6[cold]|options:area-damage] damage with a [[Reflex]] save against your class DC. A creature that fails its save also takes 2d6 persistent,cold damage.

**Source:** `= this.source` (`= this.source-type`)
