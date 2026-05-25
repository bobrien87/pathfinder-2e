---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Eagle Knight|Eagle Knight]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Mental]]", "[[Skill]]"]
prerequisites: "Eagle Knight Dedication, expert in Diplomacy"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You help an ally shake off any impediment that would give an enemy an unfair advantage. You rally a creature within 30 feet in an attempt to reduce its [[Frightened]] or [[Stupefied]] condition. If a creature has multiple conditions from this list, choose one. When you're a master in Diplomacy, add [[Clumsy]] and [[Enfeebled]] to the list of conditions. When you're legendary in Diplomacy, add [[Stunned]] to the list of conditions; if the stunned condition has a duration instead of a value, you can't use Commitment to Equality to reduce it.

Attempt a [[Diplomacy]] check against the saving throw DC of the effect that caused the condition; if there was no saving throw DC, use the hard DC for the level of the creature, hazard, or item that caused the effect. You can't treat a condition that came from an artifact or effect above 20th level unless you're legendary in Diplomacy; even if you can, the counteract DC increases by 10. You can't treat a condition that is part of a curse or disease or is a natural state of the target. Once you attempt to treat a target's condition, that target is immune to further attempts for 1 hour, regardless of the result.
- **Critical Success** Reduce the condition's value by 2.
- **Success** Reduce the condition's value by 1.
- **Critical Failure** Increase the condition's value by 1.

**Source:** `= this.source` (`= this.source-type`)
