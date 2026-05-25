---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Sorcerer]]"]
prerequisites: "Crossblooded Evolution"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your bloodline is extraordinarily complex. Choose up to three of the sorcerous gift spells granted by your secondary bloodline. You add these spells to your spell repertoire, heightened to the highest rank of spells you can cast or to the highest rank they can be heightened to that is lower than the highest rank of spells you can cast. You cast these spells as the tradition from your primary bloodline.

**Source:** `= this.source` (`= this.source-type`)
