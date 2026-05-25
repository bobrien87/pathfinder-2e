---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Nephilim]]"]
prerequisites: "any nephilim lineage feat"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have a connection to the Outer Planes, allowing you to summon a divine ally. Choose either [[Summon Celestial]], [[Summon Fiend]], or another 5th-rank spell capable of summoning an extraplanar creature appropriate to your lineage. Once per day, you can cast the chosen spell as a 5th-rank divine innate spell, but the creature summoned must be from the same category as your own lineage, such as a creature with the angel trait if you are an angelkin.

**Source:** `= this.source` (`= this.source-type`)
