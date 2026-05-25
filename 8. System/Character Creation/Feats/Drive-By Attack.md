---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Trick Driver|Trick Driver]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Trick Driver Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are piloting a vehicle.

You can smoothly line up an attack without disrupting your control.You [[Drive]], gaining the effects of the Drive action for the same number of actions you spent to Drive-By Attack. At any point during your vehicle's movement, you Strike.

**Source:** `= this.source` (`= this.source-type`)
