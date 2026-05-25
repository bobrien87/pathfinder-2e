---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Yaoguai]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You know extensively about your own kind. You gain the trained proficiency rank in Occultism. If you would automatically become trained in this skill (from your background or class, for example), you instead become trained in a skill of your choice. You also gain the [[Additional Lore]] general feat for Yaoguai Lore.

Once per day, you can gain the benefits of the [[Assurance]] feat for either Occultism or Yaoguai Lore. You choose to use this as a free action when you attempt the affected skill check.

**Source:** `= this.source` (`= this.source-type`)
