---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Druid|Druid]]"
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

You cast spells like a druid. You gain the Cast a Spell activity. You can prepare two common cantrips each day from the primal spell list or any other primal cantrips you learn or discover. You're trained in the spell attack modifier and spell DC statistics. Your key spellcasting attribute for druid archetype spells is Wisdom, and they are primal druid spells. You learn the Wildsong language, and you are bound by the druid's anathema. Choose a druidic order. You become a member of that order and are also bound by its specific anathema, allowing you to take the order's feats. You become trained in Nature and your order's associated skill; for each of these skills in which you were already trained, you become trained in a skill of your choice. You don't gain any other abilities from your choice of order.

Druid

**Source:** `= this.source` (`= this.source-type`)
