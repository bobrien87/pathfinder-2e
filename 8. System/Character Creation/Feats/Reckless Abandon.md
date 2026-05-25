---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Fortune]]", "[[Goblin]]"]
frequency: "once per day"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

Despite a lifetime filled with questionable decisions, you've managed to survive, as though you have uncanny luck that lets you avoid the consequences of your own actions. For the remainder of your turn, if you roll a failure or critical failure on a saving throw against a harmful effect, you get a success instead. Further, if you would take damage from an enemy or hazard this turn you take the minimum possible damage.

These benefits apply only to harmful effects incurred entirely during your turn in which you activate Reckless Abandon, such as running through a [[Wall of Fire]]. Persistent damage and conditions that were applied prior to your turn proceed normally, and as soon as your turn ends you are subject to the full consequences of any dangers still threatening you.

**Source:** `= this.source` (`= this.source-type`)
