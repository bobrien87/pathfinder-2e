---
type: feat
source-type: "Remaster"
level: "7"
traits: ["[[General]]", "[[Healing]]", "[[Manipulate]]", "[[Skill]]"]
prerequisites: "master in Medicine"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You use your medical training to ameliorate sickness or assuage fears. When you use Medicine to [[Administer First Aid]], instead of Stabilizing a character or Stopping Bleeding, you can reduce an ally's [[Frightened]] or [[Sickened]] condition by 2, or remove either of those conditions entirely on a critical success. You can remove only one condition at a time. The DC for the Medicine check is usually the DC of the effect that caused the condition.

**Source:** `= this.source` (`= this.source-type`)
