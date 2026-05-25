---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Samsaran]]"]
frequency: "once per day"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** You are reduced to 0 Hit Points and would gain the [[Dying]] condition or would otherwise die.

Death is as natural as breathing to you, and you can move past it as easily as the other troubles in your life. You prevent yourself from dying and regain Hit Points equal to @Damage[((6d8+floor(@actor.level/2)))[healing]]{6d8 plus half your level}. If the cause of your death was a condition or effect that would still cause you to die after regaining Hit Points, such as a high value on the [[Doomed]] condition, you suppress that effect for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
