---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Undersea Privateer|Undersea Privateer]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Undersea Privateer Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Like a flying fish, you can build up momentum and launch yourself into the air. Swim toward the surface at up to twice your swim Speed, then attempt a DC 30 [[Athletics]] check to propel yourself out of the water. If you do not swim at least 10 feet, you automatically fail. If your [[Leap]] takes you near any structure or object and have at least one hand free, you can use the `act grab-an-edge` reaction. If you do not succeed in Grabbing an Edge, you do not take any falling damage as you re-enter the water but are submerged to a distance that equals the height of your Leap.
- **Critical Success** You Leap up to 15 feet vertically and 5 feet horizontally.
- **Success** You Leap up to 10 feet vertically and 5 feet horizontally.
- **Failure** You Leap up to 5 feet vertically and 5 feet horizontally.
- **Critical Failure** You're [[Off Guard]] until the start of your next turn.

**Source:** `= this.source` (`= this.source-type`)
