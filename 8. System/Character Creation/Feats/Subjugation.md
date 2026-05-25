---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Avenging Runelord|Avenging Runelord]]"
source-type: "Remaster"
level: "16"
traits: ["[[Concentrate]]", "[[Incapacitation]]", "[[Mental]]", "[[Mythic]]"]
prerequisites: "Avenging Runelord Dedication"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have managed to gain a degree of control over the runelord's ancient soul within your mind, enough that you can project this invasive influence into the minds of others. Spend a Mythic Point. You attempt to send your runelord's influence into the mind of a creature you can sense within 30 feet. The creature attempts a [[Will]] save against your class DC or spell DC, whichever is higher. Giants take a –2 status penalty to this saving throw. Regardless of the result, the target is temporarily immune to this ability for 24 hours once the Subjugation ends.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Slowed]] 1 as it fights off your runelord's influence. You gain awareness of its abilities and weaknesses as if you achieved a critical success on a [[Recall Knowledge]] check to identify the creature.
- **Failure** The creature relinquishes control of its faculties and abilities. You gain awareness of its abilities and weaknesses as success. You control the creature until the end of its next turn.
- **Critical Failure** As failure, but you control the creature for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
