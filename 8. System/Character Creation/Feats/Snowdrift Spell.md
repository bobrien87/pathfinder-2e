---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Cold]]", "[[Druid]]", "[[Manipulate]]", "[[Spellshape]]"]
prerequisites: "storm order"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The howling wind and precipitation of your magic turn to thick snow. If your next action is to Cast a Spell that has the air, water, or cold trait, and that does not have the fire trait, select one creature affected by the spell on the ground. Each square on the ground under or adjacent to the creature fills with ankle-deep snow. Those squares are difficult terrain until the beginning of your next turn. A creature can Interact to clear a square of snow, and the snow in a square melts if that square is exposed to a fire effect.

**Source:** `= this.source` (`= this.source-type`)
