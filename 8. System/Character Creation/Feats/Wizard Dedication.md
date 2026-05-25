---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wizard|Wizard]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]", "[[Multiclass]]"]
prerequisites: "Intelligence +2"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You cast spells like a wizard, gaining a spellbook with four common arcane cantrips of your choice. You gain the [[Cast a Spell]] activity. You can prepare two cantrips each day from your spellbook. You're trained in the spell attack modifier and spell DC statistics. Your key spellcasting attribute for wizard archetype spells is Intelligence, and they are arcane wizard spells. You become trained in Arcana; if you were already trained in Arcana, you instead become trained in a skill of your choice. Select a school; you don't gain any abilities from your choice of school, but qualify for feats as a member.

Wizard

**Source:** `= this.source` (`= this.source-type`)
