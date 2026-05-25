---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Witch|Witch]]"
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

You cast spells like a witch. Choose a [[Patron]]; you gain a familiar with two common cantrips of your choice from your chosen patron's tradition, but aside from the tradition, you don't gain any other effects the patron would usually grant. Your familiar gains the normal number of abilities for a familiar instead of those a witch familiar normally gets.

You gain the [[Cast a Spell]] activity. You can prepare one cantrip each day from your familiar. You're trained in the spell attack modifier and spell DC statistics. Your key spellcasting attribute for witch archetype spells is Intelligence, and they are witch spells of your patron's tradition.

You become trained in the skill associated with the patron's tradition; if you were already trained in it, you instead become trained in a skill of your choice.

Witch

**Source:** `= this.source` (`= this.source-type`)
