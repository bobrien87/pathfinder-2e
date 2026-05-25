---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Yaoguai]]"]
prerequisites: "Yaoguai Historian"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You're adept at combating other supernatural creatures. When you succeed at a Recall Knowledge check using Occultism or Yaoguai Lore, you gain a +1 circumstance bonus to damage with weapons and unarmed attacks against that creature and all creatures of the exact same type for the next minute. If your attack would deal more than one weapon die of damage (as is common at higher levels than 1st), the bonus is equal to the number of weapon dice or unarmed attack dice. Additionally, you gain a +1 circumstance bonus to saving throws against their abilities for the next minute. For example, if you're facing three jiang-shi, you would gain these bonuses against all three of them.

**Source:** `= this.source` (`= this.source-type`)
