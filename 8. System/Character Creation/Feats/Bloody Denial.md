---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Flourish]]", "[[Guardian]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You strike a foe with force to prevent them from reacting. Make a Strike. If you hit, the target must attempt a [[Fortitude]] save saving throw against your class DC. If your Strike was a critical hit, the result of the save is one degree of success worse.
- **Critical Success** The creature is unaffected.
- **Success** Choose an ally. Until the start of your next turn, the creature can't use reactions against that ally.
- **Failure** The creature can't use reactions until the start of your next turn.
- **Critical Failure** As failure, plus the creature is [[Stunned]] 1.

**Source:** `= this.source` (`= this.source-type`)
