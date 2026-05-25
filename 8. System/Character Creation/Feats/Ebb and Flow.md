---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Spellshape]]"]
prerequisites: "Versatile Font"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can pull forth both vitality and the void simultaneously to harm your enemies and heal your allies. If your next action is to cast a 1-action or 2-action [[Heal]] or [[Harm]] spell, choose one creature in range that would be harmed by the spell, and choose another creature within range that would be healed by the spell. Your *heal* or *harm* targets both creatures.

**Source:** `= this.source` (`= this.source-type`)
