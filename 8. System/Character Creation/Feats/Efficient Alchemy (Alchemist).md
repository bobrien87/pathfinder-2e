---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Alchemist]]"]
prerequisites: "advanced alchemy"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Thanks to the time you've spent studying and experimenting, you know how to scale your formulas into larger batches that don't require any additional attention. Increase the number of items you can create each day with [[Advanced Alchemy]] to 6 + your Intelligence modifier.

In addition, when you [[Craft]] alchemical consumables during downtime, you can produce twice as many alchemical items in a single batch without spending additional preparatory time. For instance, if you are creating Elixirs of Life, you can craft up to eight elixirs in a single batch using downtime, rather than four. This doesn't change the amount of alchemical reagents or other ingredients required to craft each item, nor does it change your rate of progress for days past the base downtime spent.

**Source:** `= this.source` (`= this.source-type`)
