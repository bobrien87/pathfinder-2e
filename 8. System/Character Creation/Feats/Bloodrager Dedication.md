---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Bloodrager|Bloodrager]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Class]]", "[[Dedication]]"]
prerequisites: "Bloodrager"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Drinking powerful blood has awakened magical potential within you. You gain a spell repertoire with two cantrips of your choice, from either the arcane or divine spell list. You choose these cantrips from the common spells for your tradition or from other spells you have access to on that tradition's spell list. At least one cantrip must require a spell attack roll. You're trained in spell attack modifier and spell DC. Your key spellcasting attribute for these spells is Charisma. Spells in your repertoire gain the rage trait while you are raging, and when you Cast a Spell from your repertoire, you become [[Drained]] 1 (or increase the value of your drained condition by 1); you can reduce the value of this condition only by Harvesting Blood (see below). You become trained in Arcana if you chose arcane cantrips or Religion if you chose divine cantrips. If you were already trained in this skill, you become trained in a skill of your choice. You also gain the Harvest Blood action.

Bloodrager

**Source:** `= this.source` (`= this.source-type`)
