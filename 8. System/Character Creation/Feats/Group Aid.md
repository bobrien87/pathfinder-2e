---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Human]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your upbringing emphasized teamwork, and helping your allies comes naturally to you. After you [[Aid]] an ally at a skill check that doesn't have the attack trait, you can also Aid any other ally who attempts the same skill check for the same purpose that round. You do so as a free action rather than a reaction.

The preparation you did to help must still apply to the other allies, and you can Aid each ally only once. For example, if you helped lift up an ally to Aid them on an Athletics check to scale a wall, you could keep the same posture to give a boost to other allies attempting to scale the wall in the same round.

**Source:** `= this.source` (`= this.source-type`)
