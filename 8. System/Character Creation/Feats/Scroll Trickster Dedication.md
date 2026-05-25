---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Scroll Trickster|Scroll Trickster]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Arcana, Nature, Occultism, or Religion"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've studied scrolls in depth. This might have been a comprehensive education in formal setting, or the sort of education where you somehow obtain a number of scrolls and try not to explode anything you didn't mean to explode.

You gain the [[Trick Magic Item]] feat, and you gain a +2 circumstance bonus to skill checks to Trick scrolls. If you roll a critical failure to Trick a Magic Item that's a scroll, you get a failure instead.

Scroll Trickster

**Source:** `= this.source` (`= this.source-type`)
