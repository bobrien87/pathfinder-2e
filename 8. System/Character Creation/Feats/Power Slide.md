---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Trick Driver|Trick Driver]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Move]]", "[[Reckless]]"]
prerequisites: "Trick Driver Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are piloting a vehicle.

You throw the vehicle into a barely controlled skid, turning sharply to evade pursuit or bring your weapons to bear. You Drive with a –2 penalty to your piloting check, gaining the effects of the Drive action for the same number of actions you spent to Power Slide. At the end of the movement, if you succeed, you can turn the vehicle up to 90 degrees. If you critically succeed at your piloting check, you can instead turn the vehicle up to 180 degrees.

**Source:** `= this.source` (`= this.source-type`)
