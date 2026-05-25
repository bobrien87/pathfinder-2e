---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Golden Legionnaire|Golden Legionnaire]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Incapacitation]]", "[[Light]]", "[[Visual]]"]
prerequisites: "Golden Legionnaire Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You aren't in dim light or darkness.

You take pride in the sheen of your armor, and how useful it is at distracting your enemies when you reflect light from it. Creatures within a @Template[type:emanation|distance:5] that can see you must attempt a [[Fortitude]] save against your class DC. Once a creature attempts a save against this effect, it's temporarily immune for 24 hours.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Dazzled]] for 1 round.
- **Failure** The creature is [[Blinded]] for 1 round and dazzled for 2 rounds.
- **Critical Failure** The creature is blinded for 2 rounds and dazzled for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
