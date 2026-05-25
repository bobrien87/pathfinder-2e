---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Nephilim]]"]
prerequisites: "Angelkin, Lawbringer, Musetouched, or another lineage feat associated with celestials"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You possess celestial magic. Choose two of the following spells: [[Clear Mind]], [[Everlight]], [[Humanoid Form]], [[Revealing Light]], [[Share Life]], or [[Sure Footing]]. You can use each of the chosen spells once per day as 2nd-rank divine innate spells.

Angelkin typically take *clear mind* and *humanoid form*, lawbringers typically have *everlight* and *share life*, and musetouched typically have *revealing light* and *sure footing*.

**Source:** `= this.source` (`= this.source-type`)
