---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Earth]]", "[[Impulse]]", "[[Incapacitation]]", "[[Kineticist]]", "[[Overflow]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature damages you with an attack using an unarmed attack or a non-reach melee weapon.

Your flesh gives way as you're struck, becoming coarse sand that can magically turn your enemy to stone. You gain resistance equal to your level to physical damage from the triggering attack. The attacking creature must attempt a [[Fortitude]] save against your class DC. Regardless of the result, that creature can't trigger Calcifying Sand again for 1 hour.
- **Success** The creature is unaffected.
- **Failure** The creature is [[Slowed]] 1 until the end of its next turn.
- **Critical Failure** The creature is [[Petrified]] until the end of its next turn.

**Source:** `= this.source` (`= this.source-type`)
