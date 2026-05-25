---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wandering Chef|Wandering Chef]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Wandering Chef Dedication, expert in Crafting or Cooking Lore"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Edible morsels you create are particularly potent and bursting with flavor. When you Craft alchemical food or magical morsels that allow a saving throw, or that grants an ability that allows a saving throw, you can change its DC to your class DC or spell DC, whichever is higher. When a creature consumes alchemical food, magical morsels, or potions made by you, it also gains 5 temporary Hit Points that last for 1 hour. If you're a master in Crafting, it gains 10 temporary Hit Points instead.

> [!danger] Effect: Packed with Flavor

**Source:** `= this.source` (`= this.source-type`)
