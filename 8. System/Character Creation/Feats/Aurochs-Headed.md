---
type: feat
source-type: "Remaster"
level: "3"
traits: ["[[Skill]]"]
prerequisites: "trained in Diplomacy or Intimidation"
source: "Pathfinder #207: The Resurrection Flood"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your words and body language can subconsciously unsettle orcs, giving you an advantage when convincing them to see things your way. Many with this feat use it to travel freely between holds, warning all but the toughest orcs to waylay weaker prey. You gain a +1 circumstance bonus to skill checks to [[Make an Impression]] or [[Coerce]] creatures with the orc trait. Enemy orcs who can see you at the start of combat take a –1 penalty to initiative rolls.

**Source:** `= this.source` (`= this.source-type`)
