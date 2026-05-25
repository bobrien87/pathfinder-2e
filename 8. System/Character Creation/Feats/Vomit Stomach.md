---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Tripkee]]"]
frequency: "once per day"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You gain the [[Sickened]] condition or fail a saving throw against an ingested poison.

**Frequency** once per day

In dire circumstances you can vomit out your stomach to expel toxins. Reduce your sickened condition by 2 and immediately attempt a saving throw with a +2 circumstance bonus against any ingested poisons you have been exposed to within the last minute. You become [[Off Guard]] for 1 round as your exposed stomach makes you especially vulnerable to attacks.

**Source:** `= this.source` (`= this.source-type`)
