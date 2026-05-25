---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Monk]]", "[[Stance]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're unarmored.

You enter the stance of an unruly goat, lowering your body and preparing to butt heads with your foes. The only Strikes you can make are ramming horn attacks. These strikes deal 1d8 bludgeoning damage, are in the brawling group, and have the forceful, nonlethal, shove, and unarmed traits. When you make a ramming horn attack and your previous action was to Climb, Stride, or [[Leap]], you gain a circumstance bonus to damage equal to the number of weapon damage dice. You can make ramming horn Strikes while Climbing even if you don't have a free hand.

**Source:** `= this.source` (`= this.source-type`)
