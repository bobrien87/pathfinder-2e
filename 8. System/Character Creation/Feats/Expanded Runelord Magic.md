---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Avenging Runelord|Avenging Runelord]]"
source-type: "Remaster"
level: "14"
traits: ["[[Mythic]]"]
prerequisites: "Avenging Runelord Dedication"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your ability to use magic associated with your chosen sin grows. You gain the ability to cast one more arcane spell as an innate spell. This spell must be chosen from those listed in Avenging Runelord Dedication above, as well as [[Contingency]], [[Spell Riposte]], or any 7th-rank spell from your chosen sin's school. You can cast this spell as an arcane innate spell once per day. The spell is automatically heightened to a spell rank equal to half your level rounded up. Use mythic proficiency to determine any attack rolls or spell DCs.

**Source:** `= this.source` (`= this.source-type`)
