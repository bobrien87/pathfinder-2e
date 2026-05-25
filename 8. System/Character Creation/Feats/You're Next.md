---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Emotion]]", "[[Fear]]", "[[Mental]]", "[[Rogue]]", "[[Swashbuckler]]"]
prerequisites: "trained in Intimidation"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You reduce an enemy to 0 Hit Points.

**Rogue** After downing a foe, you menace another. Attempt to [[Demoralize]] a creature within 60 feet, with a +2 circumstance bonus. If you have legendary proficiency in Intimidation, you can use this as a free action with the same trigger.

**Swashbuckler** After downing a foe, you promise another that you're coming after them next. Attempt an Intimidation check with a +2 circumstance bonus to [[Demoralize]] a single creature that you can see and that can see you. If you're legendary in Intimidation, you can use this as a free action with the same trigger.

**Source:** `= this.source` (`= this.source-type`)
