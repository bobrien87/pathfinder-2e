---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Trick Driver|Trick Driver]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Exploration]]"]
prerequisites: "Trick Driver Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can optimize your vehicle's performance, coaxing extra speed and choosing paths to avoid slowdowns. When calculating your travel speed for the day while piloting a vehicle, you can attempt a Driving Lore check to increase your vehicle's travel speed. The DC is determined by the GM but is typically based on the vehicle's piloting DC or a difficulty based on the environment, whichever is harder. On a success, increase your vehicle's travel speed by half. This has no effect on your vehicle's movement in encounters.

**Source:** `= this.source` (`= this.source-type`)
