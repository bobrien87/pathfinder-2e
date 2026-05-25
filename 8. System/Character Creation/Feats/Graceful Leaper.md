---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Acrobat|Acrobat]]"
source-type: "Remaster"
level: "7"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Acrobat Dedication, Master in Acrobatics"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Mass and muscle are meaningless when you propel yourself through the air; only grace and balance matter.

You can roll an Acrobatics check instead of an Athletics check when making a `act high-jump skill=acrobatics` or `act long-jump skill=acrobatics`.

**Source:** `= this.source` (`= this.source-type`)
