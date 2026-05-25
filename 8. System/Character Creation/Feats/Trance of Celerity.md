---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Cursebound]]", "[[Divine]]", "[[Oracle]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your feet move faster, almost out of your conscious control. You gain a +5-foot status bonus to your Speeds for 1 minute.

If you become [[Cursebound 2]] at any point during this duration, the bonus increases to a +10-foot status bonus. If you become [[Cursebound 3]] at any point during this duration, this bonus increases to +15-foot status bonus instead. Finally, if you become [[Cursebound 4]] at any point during this duration, this bonus increases to a +20-foot status bonus.

**Source:** `= this.source` (`= this.source-type`)
