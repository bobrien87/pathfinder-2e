---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Nephilim]]"]
prerequisites: "Skillful Tail"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can perform minor mischief with your tail. You can use your tail to [[Steal]] an object, though your tail still can't hold onto it at the end of your action. If you have a hand free, you can transfer the stolen object to your hand. Otherwise, your tail surreptitiously drops it on the ground in your space, where you can grab it later. Observers other than your target who haven't witnessed you stealing something with your tail are usually distracted, meaning the GM will usually decrease their Perception DCs, as normal for Stealing something.

**Source:** `= this.source` (`= this.source-type`)
