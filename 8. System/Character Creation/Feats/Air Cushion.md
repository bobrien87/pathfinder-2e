---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Air]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature within 60 feet is falling.

Air currents flow upward to slow the target's fall to 60 feet per round. The cushion ends when the target reaches the ground, and the creature takes no damage from the fall. The cushion expires if the creature doesn't reach the ground within 1 minute, but any distance it fell during that minute doesn't count for any damage the creature would take from the fall. You can't use Air Cushion again while you have one in effect.

**Level (8th)** The range is 120 feet, and you can create cushions for up to 5 falling creatures with one reaction.

**Source:** `= this.source` (`= this.source-type`)
