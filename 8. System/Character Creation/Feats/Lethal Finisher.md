---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Death]]", "[[Finisher]]", "[[Swashbuckler]]"]
prerequisites: "precise strike 6d6"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You stab your foe in a vital organ, possibly killing them outright. Make a Strike. On a success, you forego your precise strike damage from the finisher.

Instead, your target takes additional precision damage based on a [[Fortitude]] save against your class DC. If your Strike was a critical hit, the target's saving throw outcome is one degree worse.
- **Critical Success** You deal 6 precision damage.
- **Success** You deal 6d6 precision damage.
- **Failure** You deal 12d6 precision damage.
- **Critical Failure** You deal 18d6 precision damage.

**Source:** `= this.source` (`= this.source-type`)
