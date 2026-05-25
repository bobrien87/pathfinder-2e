---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Nephilim]]"]
prerequisites: "Grimspawn, Pitborn, Hellspawn, or another lineage feat associated with fiends"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You possess fiendish magic. Choose two of the following spells: [[Disguise Magic]], [[False Vitality]], [[Invisibility]], [[See the Unseen]], [[Shatter]], or [[Paranoia]]. You can use each of the chosen spells once per day as 2nd-rank divine innate spells.

Grimspawn typically take *false vitality* and *see the unseen*, pitborn typically take *paranoia* and *shatter*, and hellspawn typically take *invisibility* and *disguise magic*.

**Source:** `= this.source` (`= this.source-type`)
