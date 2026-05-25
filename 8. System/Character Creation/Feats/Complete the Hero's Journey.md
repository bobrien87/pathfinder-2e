---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Exemplar]]", "[[Healing]]", "[[Transcendence]]"]
frequency: "once per PT10M"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

**Requirements** You have Sparked Transcendence of at least two different ikons in the last 10 minutes, and your divine spark currently dwells in a third ikon.

As your divine spark travels through each of your ikons in turn, it gains power, culminating its journey when it enters your third ikon. You Spark Transcendence of your final ikon, but instead of its normal effect, the item casts the 3-action version of [[Harm]] or [[Heal]] heightened to half your level rounded up.

**Source:** `= this.source` (`= this.source-type`)
