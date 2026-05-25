---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Bard]]"]
prerequisites: "polymath muse"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can rely on the grandeur of your performances rather than ordinary social skills. You can use Performance instead of Diplomacy to `act make-an-impression statistic=performance` and instead of Intimidation to `act demoralize statistic=performance`. You can also use an acting Performance instead of Deception to `act impersonate statistic=performance`.

In addition, you can use your proficiency rank in Performance to meet the prerequisites of skill feats that require a particular proficiency rank in Deception, Diplomacy, or Intimidation.

**Source:** `= this.source` (`= this.source-type`)
