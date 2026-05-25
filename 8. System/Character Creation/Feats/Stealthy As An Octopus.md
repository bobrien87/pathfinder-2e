---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Undersea Privateer|Undersea Privateer]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Undersea Privateer Dedication, expert in Stealth"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You're an expert at using the dark of the ocean to conceal yourself. As long as you're separated from a creature by 20 or more feet of water, the turbulence of the water grants you enough cover to attempt to `act hide` from that creature.

**Source:** `= this.source` (`= this.source-type`)
