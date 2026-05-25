---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Druid]]"]
frequency: "once per PT1H"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

You raise a druidic monument, such as a standing stone or warding tree, from the ground, creating a powerful primal ward that blocks other types of magic. The monument appears in an unoccupied square on the ground within 30 feet, making that square difficult terrain. Choose arcane, divine, or occult; all creatures within @Template[emanation|distance:15]{15 feet} of the monument gain a +2 status bonus to their saving throws against effects with that trait. The monument lasts for 1 round before crumbling back into the earth or wilting away into nothingness, but you can Sustain the monument for up to 1 minute.

> [!danger] Effect: Raise Menhir

**Source:** `= this.source` (`= this.source-type`)
