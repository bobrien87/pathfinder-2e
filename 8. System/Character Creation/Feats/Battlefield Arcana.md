---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/War Mage|War Mage]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Spellshape]]"]
prerequisites: "Steady Spellcasting"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have learned to safely cast spells even in the heat of battle. If the next action you use is to cast a wizard cantrip, or a wizard spell that is at least 2 ranks lower than the highest-rank wizard spell slot you have, that spell does not trigger reactions that normally trigger due to a spell being cast or someone using an action with the manipulate trait.

**Source:** `= this.source` (`= this.source-type`)
