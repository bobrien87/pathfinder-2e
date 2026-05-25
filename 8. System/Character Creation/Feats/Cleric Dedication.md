---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Cleric|Cleric]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]", "[[Multiclass]]"]
prerequisites: "Wisdom +2"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You cast spells like a cleric. You gain the Cast a Spell activity. You can prepare two common cantrips each day from the divine spell list or any other divine cantrips you have access to. You're trained in the spell attack modifier and spell DC statistics. Your key spellcasting attribute for cleric archetype spells is Wisdom, and they are divine cleric spells. Choose a deity as you would if you were a cleric. You become bound by that deity's anathema and can receive that deity's divine sanctification. You become trained in Religion and your deity's associated skill; for each of these skills in which you were already trained, you instead become trained in a skill of your choice. You don't gain any other abilities from your choice of deity.

Cleric

**Source:** `= this.source` (`= this.source-type`)
