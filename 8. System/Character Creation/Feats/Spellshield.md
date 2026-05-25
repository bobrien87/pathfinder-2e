---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/War Mage|War Mage]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "War Mage Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your shield becomes a bonded item capable of storing your spells. You gain the [[Arcane Bond]] class feature and the [[Drain Bonded Item]] action. You must select a shield as your bonded item. When you make your daily preparations, you can prepare one fewer wizard spell to infuse that magic into your bonded item. This spell must be at least 1 rank lower than the highest-rank wizard spell slot you have. When you Drain your Bonded Item to Cast a Spell, that spell is automatically heightened to the rank of spell you infused into your shield, no matter what rank you originally prepared it at.

**Source:** `= this.source` (`= this.source-type`)
