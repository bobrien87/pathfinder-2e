---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Inventor]]"]
prerequisites: "construct innovation"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your construct unleashes a broad swath of devastation by separating its limbs, deploying hidden armaments, or using a similar technique to wreak havoc. You Command your innovation. Instead of its normal actions, it Strides once, then makes a Strike against each foe within 30 feet of it with a +2 circumstance bonus to its attack rolls. The multiple attack penalty doesn't increase until after the construct makes all the attacks.

> [!danger] Effect: Engine of Destruction

**Source:** `= this.source` (`= this.source-type`)
