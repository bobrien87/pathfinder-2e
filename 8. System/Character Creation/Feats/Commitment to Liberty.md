---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Eagle Knight|Eagle Knight]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Eagle Knight Dedication"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** A creature has an ally [[Grabbed]] or [[Restrained]].

You can't abide when a foe has one of your allies in its grip. Make a Strike against the required creature. If this Strike hits, the grabbed or restrained ally can immediately attempt to [[Escape]] as a free action. If the Strike was a critical hit, that ally gains a +2 circumstance bonus to their Escape attempt.

**Source:** `= this.source` (`= this.source-type`)
