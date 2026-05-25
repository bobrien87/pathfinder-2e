---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Auditory]]", "[[Commander]]", "[[Incapacitation]]", "[[Mental]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You and your allies currently outnumber enemies on the battlefield, and you or an ally has either [[Restrained]] an opponent or reduced an opponent to 0 Hit Points since the start of your last turn.

Confident in your victory, you command your opponent's surrender. Choose one opponent you are observing. You command that opponent to surrender in a strong voice. They must attempt a [[Will]] save against your class DC, with the following results.
- **Critical Success** The creature is unaffected.
- **Success** The creature cannot take any hostile actions that include you as a target for 1 round.
- **Failure** As success, and the target is [[Fleeing]] for 1 round.
- **Critical Failure** The creature drops any weapons or items it is holding, lies [[Prone]] on the ground, and does not take any hostile actions against you or your allies for 1 minute, or until you or one of your allies attacks it.

**Source:** `= this.source` (`= this.source-type`)
