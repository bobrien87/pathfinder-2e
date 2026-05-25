---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Timewracked|Timewracked]]"
source-type: "Remaster"
level: "18"
traits: ["[[Incapacitation]]", "[[Mythic]]", "[[Occult]]"]
prerequisites: "Timewracked Dedication"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your ability to interact with and even observe the flow of time allows you to fracture it slightly in a localized place whenever you land a particularly solid blow on a foe. Whenever you achieve a critical success with a Strike, the target of that Strike must also attempt a [[Will]] save against your class DC or spell DC, whichever is higher.
- **Critical Success** The target is unaffected by the fractured timeflow.
- **Success** The target is [[Slowed]] 1 for 1 round.
- **Failure** The target is [[Slowed]] 2 for 1 round.
- **Critical Failure** The target is [[Stunned]] 3, then slowed 2 for 1 round after they recover from being stunned.

**Source:** `= this.source` (`= this.source-type`)
