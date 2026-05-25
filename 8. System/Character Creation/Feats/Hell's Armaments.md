---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Hellknight|Hellknight]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Hellknight Preferment, expert in at least one of your order's favored weapons"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've trained relentlessly with your order's weapon to maximize their deadliness. When you get a critical success on a Strike with one of your order's favored weapons, the target must attempt a [[Fortitude]] save against your class DC. If you have access to that weapon's critical specialization effect, you must choose whether to use that effect or this one.
- **Critical Success** The target is unaffected.
- **Success** The target takes a –10-foot circumstance penalty to its Speeds until the end of your next turn.
- **Failure** As success, and the target is [[Slowed]] 1 until the end of your next turn.
- **Critical Failure** As success, and the target is [[Slowed]] 2 until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
