---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Oatia Skysage|Oatia Skysage]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Occultism"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your study of the stars unlocks supernatural insights and magic. You either become trained in Astronomy Lore or an expert in Occultism.

You learn to cast spontaneous spells and gain the Cast a Spell activity. You gain a spell repertoire with two of the following cantrips of your choice: [[Detect Magic]], [[Guidance]], [[Know the Way]], or [[Read Aura]]. You cast these spells as occult spells as you draw on the stars and night sky. You're trained in occult spell attack rolls and spell DCs. Your key spellcasting ability for these spells is Intelligence.

Oatia Skysage

**Source:** `= this.source` (`= this.source-type`)
