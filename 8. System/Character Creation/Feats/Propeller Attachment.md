---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Trapsmith|Trapsmith]]"
source-type: "Remaster"
level: "7"
traits: ["[[Archetype]]"]
prerequisites: "Trapsmith Dedication, master in Crafting"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've mastered attaching clockwork propellers to your daily quick-deploy snares that use gears. This allows you to place your snares in the air or underwater, where they remain in place for up to 10 minutes, after which the propeller runs out of power and they fall or sink. Unless you use additional precautions to hide it, a propeller snare's location is usually obvious.

**Source:** `= this.source` (`= this.source-type`)
