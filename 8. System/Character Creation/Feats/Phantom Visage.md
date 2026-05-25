---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Goblin]]", "[[Illusion]]", "[[Occult]]", "[[Visual]]"]
prerequisites: "dokkaebi goblin heritage"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You cloak yourself in illusions to mask your nature. Your Phantom Visage is a specific alternate form of a Small or Medium humanoid ancestry prevalent where you grew up (typically human), though it doesn't need to have analogous physical features to your natural goblin form. Your Phantom Visage counts as setting up a disguise for the [[Impersonate]] use of Deception. If you use any unarmed attacks you gained from a goblin heritage or ancestry feats while in your Phantom Visage, the illusion immediately breaks. You can maintain your Phantom Visage indefinitely, and you can shift back to your true goblin form by using this action again.

**Source:** `= this.source` (`= this.source-type`)
