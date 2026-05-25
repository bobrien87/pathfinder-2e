---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Vigilante|Vigilante]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "expert in Arcana, Nature, Occultism, or Religion, Vigilante Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've learned to hide the magical auras of your gear. During your daily preparations, you carefully tweak any or all of your magic items to appear non-magical. Objects adjusted in this way remain so until your next preparations.

A spellcaster using [[Detect Magic]] or [[Read Aura]] must succeed at a Perception check against your Deception DC to see through your obfuscations.

**Source:** `= this.source` (`= this.source-type`)
