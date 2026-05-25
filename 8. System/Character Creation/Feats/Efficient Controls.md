---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Vehicle Mechanic|Vehicle Mechanic]]"
source-type: "Remaster"
level: "7"
traits: ["[[Archetype]]"]
prerequisites: "Vehicle Mechanic Dedication, master in Crafting"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

By reducing redundant systems and streamlining essential functions, you have made it easier for the vehicle to operate with fewer crew. Reduce the number of crew required to operate your signature vehicle by 25%. For example, you would reduce a sailing ship from needing 1 pilot and 8 crew to 1 pilot and 6 crew. This adjustment only affects the number of crew needed to operate the vehicle; it doesn't reduce the vehicle's need for a pilot.

**Source:** `= this.source` (`= this.source-type`)
