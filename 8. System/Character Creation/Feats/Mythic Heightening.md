---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wildspell|Wildspell]]"
source-type: "Remaster"
level: "14"
traits: ["[[Concentrate]]", "[[Mythic]]", "[[Spellshape]]"]
prerequisites: "Wildspell Dedication"
frequency: "once per day"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You overload your minor spells to give them greater effect. Spend a Mythic Point. If the next action you use is to Cast a Spell, that spell is heightened to the highest spell rank that you can cast. Any spell attack roll is made with mythic proficiency, and the spell's DC is calculated with mythic proficiency. The spell slot used to cast the spell isn't changed.

**Source:** `= this.source` (`= this.source-type`)
