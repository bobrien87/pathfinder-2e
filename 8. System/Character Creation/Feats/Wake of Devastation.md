---
type: feat
source-type: "Remaster"
level: "20"
traits: ["[[Monk]]"]
prerequisites: "Kaiju Stance"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're in [[Kaiju Stance]].

Like a kaiju, you leave a trail of destruction in your wake. Your shattering earth attacks gain the razing trait. Whenever you succeed with a shattering earth attack while standing on the ground, the earth buckles under the force of the blow, and all the squares beneath you become difficult terrain.

Whenever you critically succeed with a shattering earth attack against a creature standing on the ground in an area of difficult terrain, you pummel the creature into the earth; they become [[Immobilized]] until they succeed at an [[Escape]] attempt against your class DC.

**Source:** `= this.source` (`= this.source-type`)
