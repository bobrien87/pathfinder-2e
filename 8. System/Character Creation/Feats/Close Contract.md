---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Blackjacket|Blackjacket]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Concentrate]]"]
prerequisites: "Mercenary Motivation"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have completed your active course of action but haven't Dismissed it or chosen a new one.

You're bolstered when a plan comes together. You Dismiss your current course of action and gain 15 temporary Hit Points that last for 1 hour. The number of temporary Hit Points increases by 5 at 12th level and every 2 levels thereafter.

**Source:** `= this.source` (`= this.source-type`)
