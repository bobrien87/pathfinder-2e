---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Rogue]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A trap within your reach is triggered.

You try to jam the workings of a trap to delay its effects. Attempt a Thievery check to [[Disable a Device]] on the trap with the following results instead of the normal ones for the action.
- **Critical Success** You either prevent the trap from being triggered or delay the activation until the start or end of your next turn.
- **Success** As above, but the GM chooses whichever is worse for you.
- **Failure** No effect.
- **Critical Failure** You're [[Off Guard]] until the start of your next turn.

**Source:** `= this.source` (`= this.source-type`)
