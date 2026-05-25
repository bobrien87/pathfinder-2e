---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wandering Chef|Wandering Chef]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Morning Side Dishes"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your techniques extend the storage life for certain ingredients and food through pickling, alcohol, or fermentation. When you use advanced alchemy to create alchemical food, you can designate one infused item to not automatically expire when you next make your daily preparations. When you preserve another item in this way, the previous item becomes inedible.

The number of items you can preserve during your daily preparation and the maximum number of items you can have preserved before spoiling older items increases to two if you're an expert in Crafting or Cooking Lore, to three if you're a master, and to five if you're legendary.

**Source:** `= this.source` (`= this.source-type`)
