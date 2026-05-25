---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "expert in Crafting"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can have other PCs help you [[Craft]] an item, under your direction. A helper PC rolls a check with a skill in which they're trained. The skill must be Crafting or another skill relevant to the item, as determined by the GM. For example, a PC might use Religion to help you Craft an item with the divine trait or Warfare Lore to help you Craft a weapon. Your roll still determines whether you successfully create the item. Any helper's roll contributes toward reducing the cost of raw materials using the numbers from the [[Earn Income]] table; this uses the ally PC's proficiency rank in the skill and their level – 1 for their level. Helping PCs must accompany you throughout the Craft activity (preventing them from pursuing other downtime activities) or the benefit is lost. The GM might determine that only a certain number of PCs can help depending on the circumstances. Communal Crafting also allows you to take the role of a helper when someone else is crafting, provided they accept your help.

**Source:** `= this.source` (`= this.source-type`)
