---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Undersea Privateer|Undersea Privateer]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Attack]]", "[[Manipulate]]"]
prerequisites: "Anchor Stance"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're in Anchor Stance, and your target is within 5 feet of the edge of a water vehicle or already in the water.

You swirl water around you to make a current that pulls creatures closer. Attempt an Athletics check against the Fortitude DC of a creature within 20 feet. If the creature is willing, you increase your degree of success by one (turning a failure into a success and a success into a critical success).
- **Critical Success** The target is pulled 10 feet toward you.
- **Success** The target is pulled 5 feet toward you.
- **Critical Failure** Your movements cause you to be [[Off Guard]] until the beginning of your next turn.

**Source:** `= this.source` (`= this.source-type`)
