---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Fighter]]"]
prerequisites: "Dueling Riposte"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your weapon whirls and darts, striking foes whenever the slightest opening or moment of weakness presents itself. You can use [[Dueling Riposte]] even if you aren't benefiting from [[Dueling Parry]] (though you must be wielding a single one-handed weapon and nothing else). At the start of each of your turns, you gain an additional reaction that you can use only to make a Dueling Riposte.

**Source:** `= this.source` (`= this.source-type`)
