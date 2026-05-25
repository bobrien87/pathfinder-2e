---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Dwarf]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your innate connection to stone makes you adept at moving across uneven surfaces. You can ignore difficult terrain caused by stone (such as rubble or gravel) and uneven ground made of stone and earth. In addition, when you use the Acrobatics skill to [[Balance]] on narrow surfaces or uneven ground made of stone or earth, you aren't [[Off Guard]], and when you roll a success at one of these Acrobatics checks, you get a critical success instead.

**Source:** `= this.source` (`= this.source-type`)
