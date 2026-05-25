---
type: feat
source-type: "Remaster"
level: "15"
traits: ["[[Emotion]]", "[[Fear]]", "[[General]]", "[[Incapacitation]]", "[[Skill]]"]
prerequisites: "legendary in Intimidation"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can frighten foes so much, they might die. Attempt an [[Intimidation]] check against the Will DC of a living creature within 30 feet of you that you sense or observe and who can sense or observe you. If the target can't hear you or doesn't understand the language you are speaking, you take a –4 circumstance penalty. The creature is temporarily immune for 1 minute.
- **Critical Success** The target must attempt a [[Fortitude]] save against your Intimidation DC. On a critical failure, it dies. On any other result, it becomes [[Frightened]] 2 and is [[Fleeing]] for 1 round. The critical failure effect has the death trait.
- **Success** The target becomes frightened 2.
- **Failure** The target becomes [[Frightened]] 1.
- **Critical Failure** The target is unaffected.

**Source:** `= this.source` (`= this.source-type`)
