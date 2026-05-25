---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Divine]]", "[[Illusion]]", "[[Nephilim]]", "[[Polymorph]]"]
prerequisites: "Faultspawn"
frequency: "once per PT1H"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

You fill an area with your force of will, towering beyond where your true form should be. Increase your size to Large until the beginning of your next turn. Your equipment grows with you but returns to natural size if removed. You're [[Clumsy]] 1. Your reach increases by 5 feet (or by 10 feet if you started out Tiny), and you gain a +2 status bonus to melee damage. Towering Presence has no effect if you were already Large or larger.

**Source:** `= this.source` (`= this.source-type`)
