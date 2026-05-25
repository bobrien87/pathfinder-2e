---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Barbarian]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You fall at least 10 feet and land on a solid surface.

You slam into the ground, shattering it around you. Treat the fall as 10 feet shorter. You land on your feet. The ground in a @Template[emanation|distance:5] becomes difficult terrain. Any creature in the emanation when you land takes @Damage[5[bludgeoning]|options:area-damage] damage as the debris hits it and is [[Off Guard]] until the start of its next turn.

**Source:** `= this.source` (`= this.source-type`)
