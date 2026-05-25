---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Dragonblood]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can briefly transform into a paragon of your draconic ancestry. You can cast [[Dragon Form]] as an 8th-rank innate spell once per day. This spell has the same tradition as your draconic exemplar. When you cast this innate spell, you must transform into your draconic exemplar. However, if you have the [[Arcane Dragonblood]], [[Divine Dragonblood]], [[Occult Dragonblood]], or [[Primal Dragonblood]] lineage feat, you can instead choose any dragon of that tradition.

**Source:** `= this.source` (`= this.source-type`)
