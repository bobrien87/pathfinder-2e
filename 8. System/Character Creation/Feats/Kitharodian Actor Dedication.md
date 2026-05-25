---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Kitharodian Actor|Kitharodian Actor]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Performance"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You are from Taldor or have attended Kitharodian Academy.

You've studied classic Taldan theater and learned to embody various roles to a sublime degree. You become trained in Society and in Theater Lore; if you were already trained in either, you become an expert in that skill instead. In addition, when you attempt a Deception or Performance check to portray a famous figure, you gain a +2 circumstance bonus to your check. This bonus changes to +3 at 10th level and +4 at 17th level. However, you don't gain this bonus while Impersonating a figure whose death is common knowledge (as determined by the GM).

Kitharodian Actor

**Source:** `= this.source` (`= this.source-type`)
