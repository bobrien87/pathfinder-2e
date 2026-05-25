---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Undersea Privateer|Undersea Privateer]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Undersea Privateer Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You're practiced at scaling ships, and even a wet and slippery exterior won't stand in your way. You can Climb a sea vehicle even if you have one hand occupied. If both your hands are free, you gain a +2 circumstance bonus to your Athletics check. You aren't [[Off Guard]] while Balancing or Climbing on any part of a sea vehicle.

**Source:** `= this.source` (`= this.source-type`)
