---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Cleric]]", "[[Divine]]"]
prerequisites: "Raise Symbol"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** While you have your symbol raised, you are about to take damage from a melee attack.

Your religious symbol glows with sacred energy, turning the attacker's strength to weakness. Attempt a [[Religion]] check against the triggering creature's Will DC. Regardless of the result, the creature is temporarily immune for 1 minute.
- **Critical Success** The creature is [[Enfeebled]] 2 until it spends at least 1 action moving away from you.
- **Success** As critical success, but [[Enfeebled]] 1.

**Source:** `= this.source` (`= this.source-type`)
