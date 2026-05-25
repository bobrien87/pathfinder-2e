---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Lizardfolk]]"]
prerequisites: "River Adaptation"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

`pf2:2` or `pf2:3`

**Requirements** You are swimming and have a free hand.

The waters around you permit you passage, a privilege you can share with a willing ally. You hold on to an adjacent ally and Swim, carrying them along with you. If you spend three actions Ferrying through Waves, you instead Swim twice. If your ally would need to attempt any Athletics checks to Swim while you're Ferrying through Waves, you roll the check and your result applies to them.

**Source:** `= this.source` (`= this.source-type`)
