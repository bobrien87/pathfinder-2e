---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Champion]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your faith makes you resistant to disease, protecting you as you offer succor to the ill. You gain a +2 status bonus to saves against diseases and poisons and to flat checks to recover from persistent poison damage. Allies in your champion's aura get this benefit, but their bonus is +1.

In addition, if you roll a success on a save against a disease or poison, you get a critical success instead. (Your allies don't share this benefit.) If you have the [[Sacred Body]] class feature, when you roll a critical failure on a save against a disease or poison, you get a failure instead.

**Source:** `= this.source` (`= this.source-type`)
