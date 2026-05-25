---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Automaton]]"]
prerequisites: "Hunter automaton"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have developed magical techniques to aid you with stalking your prey. You can cast [[Blur]] and [[Invisibility]] each once per day as 2nd-rank arcane innate spells.

**Enhancement** Your camouflage is more potent. Your blur spell now lasts 10 minutes and when you cast invisibility, you can choose to gain the effects of the 4th-rank version of the spell. In addition, you can now cast blur and invisibility each twice per day.

**Source:** `= this.source` (`= this.source-type`)
