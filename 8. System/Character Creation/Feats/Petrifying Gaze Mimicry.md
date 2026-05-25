---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wild Mimic|Wild Mimic]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Incapacitation]]", "[[Primal]]", "[[Visual]]"]
prerequisites: "Wild Mimic Dedication, you have attempted a saving throw against a creature's petrifying gaze or a similar ability or have identified a creature with such an ability in combat"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Either by witnessing or surviving the petrifying stare of a medusa or similar creature, you have learned to petrify those you lock eyes with. You stare at a creature you can see within 30 feet. The creature attempts a [[Fortitude]] save against the higher of your class DC or spell DC. You must wait 1d4 rounds before using this ability again.
- **Critical Success** The creature is unaffected and temporarily immune to your Petrifying Gaze Mimicry for 24 hours.
- **Success** The creature is [[Slowed]] 1 for 1 round.
- **Failure** The creature is slowed 1 for 1 round and [[Immobilized]] for 1 round or until it [[Escapes]].
- **Critical Failure** The creature is [[Slowed]] 2 for 1 round and immobilized until it Escapes.

**Source:** `= this.source` (`= this.source-type`)
