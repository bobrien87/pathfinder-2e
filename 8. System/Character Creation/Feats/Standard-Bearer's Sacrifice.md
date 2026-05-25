---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Brandish]]", "[[Commander]]", "[[Manipulate]]", "[[Visual]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An opponent targets an ally with a ranged attack, you are observing both of them, and you are also in range of the attack.

**Requirements** You are holding or wielding your banner.

Seeing an enemy take aim at your ally, you bravely flourish your banner to redirect their attention to you. The triggering opponent must attempt a [[Will]] save against your class DC.
- **Success** The opponent completes its attack against your ally.
- **Failure** The opponent targets you with the triggering attack instead.
- **Critical Failure** As failure, and you gain a +2 circumstance bonus to your AC against the triggering attack.

**Source:** `= this.source` (`= this.source-type`)
