---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Nagaji]]"]
prerequisites: "nagaji venomous spit unarmed attack"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can store prepared venom in your throat and spit it at your foes in addition to your own toxic spray. You can Interact to store a dose of injury or touch poison in your throat; when using this action, you do not risk envenoming yourself as long as the poison is your level or lower. The next time you attack a target with your venomous spit unarmed attack, the poison is expended. If you successfully hit the target, they are exposed to the poison in addition to the other effects of your spit. As long as you are holding venom in your throat, your speech is noticeably difficult to understand. You can hold only one dose of poison like this at a time.

**Source:** `= this.source` (`= this.source-type`)
