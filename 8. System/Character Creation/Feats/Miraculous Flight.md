---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Vehicle Mechanic|Vehicle Mechanic]]"
source-type: "Remaster"
level: "18"
traits: ["[[Archetype]]", "[[Magical]]"]
prerequisites: "Vehicle Mechanic Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With superior engineering and magical application, you have freed your signature vehicle from the bonds of gravity, allowing it to soar through the sky like a dragon. The vehicle gains magical propulsion and a fly Speed equal to its fastest current Speed. If your signature vehicle already had a fly Speed, reduce the distance the vehicle needs to make a 90-degree turn to half the usual length (typically half the length of the vehicle).

**Source:** `= this.source` (`= this.source-type`)
