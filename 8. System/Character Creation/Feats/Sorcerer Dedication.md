---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Sorcerer|Sorcerer]]"
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

Choose a [[Bloodline]]. You become trained in the bloodline's two skills; for each of these skills in which you were already trained, you become trained in a skill of your choice.

You cast spells like a sorcerer. You gain access to the Cast a Spell activity. You gain a spell repertoire with two common cantrips from the spell list associated with your bloodline, from the spells granted by your bloodline, or any other cantrips of that tradition you learn or discover. You're trained in the spell attack modifier and spell DC statistics. Your key spellcasting attribute for sorcerer archetype spells is Charisma, and they are sorcerer spells of your bloodline's tradition. You don't gain any other abilities from your choice of bloodline.

Sorcerer

**Source:** `= this.source` (`= this.source-type`)
