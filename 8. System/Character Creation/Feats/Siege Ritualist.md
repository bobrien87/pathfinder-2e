---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/War Mage|War Mage]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "War Mage Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Sometimes, magical warfare requires the application of more complex arcana. When you attempt a Warfare Lore check as one of the casters of a ritual, you gain a +2 circumstance bonus to the check. You learn a siege ritual of 2nd rank or lower. You must meet all prerequisites to be the primary caster of a ritual to select it.

At 8th level and every 4 levels thereafter, you learn another siege ritual with the same restriction and with a maximum rank of half that level.

**Source:** `= this.source` (`= this.source-type`)
