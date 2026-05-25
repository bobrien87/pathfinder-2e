---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Ranger]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can react with ranged weapons when a creature is in close quarters. You can use a reaction that normally allows you to make a melee weapon Strike to instead make a ranged weapon Strike. You must be Striking an adjacent target. If necessary for the reaction's trigger, you treat your ranged weapon as if it had a reach of 5 feet. If the reaction has other requirements, such as wielding a specific kind of weapon, Snap Shot doesn't allow you to ignore them; it allows you only to replace a melee weapon Strike with a ranged weapon Strike.

**Source:** `= this.source` (`= this.source-type`)
