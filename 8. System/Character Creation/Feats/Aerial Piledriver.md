---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wrestler|Wrestler]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Attack]]"]
prerequisites: "Wrestler Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have a creature [[Grabbed]] or [[Restrained]].

Heaving both yourself and your opponent into the air, you bring them crashing to the ground. Make an unarmed melee Strike against the creature you have grabbed or restrained. This Strike deals 1d6 additional damage per weapon damage die, and it has the following additional effects on a success, failure, and critical failure.
- **Success** The target lands [[Prone]].
- **Failure** You lose your grip on the target, and it is no longer grabbed or restrained by you.
- **Critical Failure** You lose both your grip on the target and your balance. You fall prone, and the target is no longer grabbed or restrained by you.

**Source:** `= this.source` (`= this.source-type`)
