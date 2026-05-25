---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Exploration]]", "[[Investigator]]"]
prerequisites: "Clue Them All In"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You spend 1 minute briefing up to four allies about one of your open investigations. Those allies gain the same circumstance bonus you do from [[Pursue a Lead]] to checks to investigate the question at the heart of that investigation. This bonus lasts until you cease Pursing that Lead or for 1 day, whichever comes first. This doesn't confer any other benefits of pursuing a lead, such as adding the circumstance bonus to your saves with [[Detective's Readiness]].

**Source:** `= this.source` (`= this.source-type`)
