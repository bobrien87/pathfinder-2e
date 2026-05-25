---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Oracle|Oracle]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]", "[[Multiclass]]"]
prerequisites: "Charisma +2"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Choose a [[Mystery]].You become trained in Religion and the mystery's skill; if you were already trained, you become trained in a skill of your choice. You gain the curse associated with your mystery, which follows the normal rules for an oracular curse.

You cast spells like an oracle and gain the Cast a Spell activity. You gain a spell repertoire with two cantrips, either common divine cantrips or other divine cantrips you learn or discover. You're trained in the spell attack modifier and spell DC statistics. Your key spellcasting attribute for oracle archetype spells is Charisma, and they are divine oracle spells.

Oracle

**Source:** `= this.source` (`= this.source-type`)
