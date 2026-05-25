---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Runelord|Runelord]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Runelord Dedication"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your personal rune is connected more closely to your arcane bond. You gain the critical specialization effects of your arcane bonded weapon. In addition, whenever you critically hit a creature with your arcane bonded weapon, they begin to feel the pull of your sin, imposing a –2 circumstance penalty to saves against any of your curriculum or sin spells until the end of your next turn.

> [!danger] Effect: Rod of Rule

**Source:** `= this.source` (`= this.source-type`)
