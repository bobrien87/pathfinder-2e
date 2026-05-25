---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Incapacitation]]", "[[Occult]]", "[[Sarangay]]"]
frequency: "once per day"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

Your dedication to the ideals of art and beauty allows your head gem to access the power of the waning moon. While you possess your head gem, you can overwhelm foes with a sense of reverent wonder. Enemies within a @Template[emanation|distance:15] must attempt a [[Will]] save against the higher of your class DC or spell DC.
- **Critical Success** The enemy is unaffected.
- **Success** The enemy is [[Fascinated]] for 1 round.
- **Failure** The enemy is [[Stunned]] 1.
- **Critical Failure** The enemy is [[Paralyzed]] for 1 round.

**Source:** `= this.source` (`= this.source-type`)
