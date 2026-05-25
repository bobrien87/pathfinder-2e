---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Guardian]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With a powerful blow, you crack a foe's armor or tough hide, opening it up for further attacks. Make a melee Strike. This Strike deals one additional weapon die of damage; if the target is your taunted enemy, this increases to two additional weapon die of damage. This counts as two attacks for the purposes of calculating your multiple attack penalty. If you hit and deal damage, the target must attempt a [[Fortitude]] save saving throw against your class DC.
- **Critical Success** The target takes no additional effect.
- **Success** The target is [[Off Guard]] until the end of your next turn.
- **Failure** The target is [[Clumsy]] 2 until the end of your next turn. Once it loses this clumsy condition, it's off-guard for 1 round.
- **Critical Failure** As failure, but the target is [[Clumsy]] 3.

**Source:** `= this.source` (`= this.source-type`)
