---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Concentrate]]", "[[Druid]]", "[[Spellshape]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You fold your spell into a seed. If your next action is to Cast a Spell using 1 action or 2 actions, the spell instead plants itself in an adjacent square. You must make all decisions regarding the spell at the time you cast it. Within the next 10 minutes, you can direct your sown spell to sprout and produce the spell's effects as a reaction, which is triggered when a creature enters the sown spell's space or a square adjacent to it. You can have only one sown spell at a time, and if you don't trigger the spell within 10 minutes, it dissipates and the spell is lost. A creature can notice the sown spell with a successful [[Perception]] check against your spell DC.

**Source:** `= this.source` (`= this.source-type`)
