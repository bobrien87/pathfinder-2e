---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Incapacitation]]", "[[Rogue]]"]
prerequisites: "Debilitating Strike"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your debilitations are especially effective on your most powerful attacks. Whenever you critically succeed at an attack roll against an enemy and use Debilitating Strike, add the following debilitation to the list you can choose from.

- **Debilitation** The target attempts a [[Fortitude]] save against your class DC with the following effects.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Slowed]] 1 until the end of your next turn.
- **Failure** The target is [[Slowed]] 2 until the end of your next turn.
- **Critical Failure** The target is [[Paralyzed]] until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
