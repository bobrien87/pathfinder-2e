---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sentinel|Sentinel]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have trained carefully to maximize the protective qualities of your armor. You become trained in light armor and medium armor. If you already were trained in light armor and medium armor, you gain training in heavy armor as well. Whenever you gain a class feature that grants you expert or greater proficiency in any type of armor (but not unarmored defense), you also gain that proficiency in the armor types granted to you by this feat. If you have a class feature that grants you expert proficiency in unarmored defense and you're 13th level or higher, you also become an expert in the armor types granted to you by this feat.

Sentinel

**Source:** `= this.source` (`= this.source-type`)
