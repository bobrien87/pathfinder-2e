---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Air]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

A speeding wind heeds your call, picking someone up and depositing them nearby. Choose a creature within 60 feet of you. The target jumps in any direction, up to a maximum of 30 feet. If the target doesn't land on a space of solid ground within 30 feet of where it started, it falls unless it has a fly Speed but doesn't take any damage from the fall. You choose the distance and direction of the jump. If you target an unwilling creature, it attempts a [[Reflex]] save against your class DC with the following results.
- **Success** The creature is unaffected.
- **Failure** You make the creature jump up to half the maximum distance.
- **Critical Failure** You make the creature jump up to the maximum distance.

**Level (+2)** The maximum distance increases by 15 feet.

**Source:** `= this.source` (`= this.source-type`)
