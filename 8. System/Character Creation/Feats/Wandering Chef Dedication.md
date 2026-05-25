---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wandering Chef|Wandering Chef]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Whether trained in a noble kitchen or a humble home, you know how to cook delicious dishes and source ingredients from the wilderness or urban settings. You become trained in Crafting; if you were already trained in Crafting, you instead become trained in a skill of your choice. You can use cookware instead of an alchemist's toolkit to craft alchemical foods. When using the [[Subsist]] downtime activity, you can use Crafting or Cooking Lore in place of Survival, and if you roll a failure, you get a success instead.

You gain the Quick Alchemy benefits, but can use it only to create consumables, and the consumables must be alchemical food. Any items you choose with [[Alchemical Crafting]] must be alchemical food, but they can be 1st level or 2nd level instead of only 1st level.

You create up to 4 versatile vials during your daily preparations. Typically, a wandering chef's versatile vials take the form of parcels of foraged ingredients.

Wandering Chef

**Source:** `= this.source` (`= this.source-type`)
