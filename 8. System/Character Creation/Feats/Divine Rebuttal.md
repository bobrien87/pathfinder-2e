---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Cleric]]", "[[Divine]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** Your ally is about to roll a saving throw against a magical ability of a creature you're adjacent to.

**Requirements** You are wielding your deity's favored weapon.

You strive against magical threats physically and spiritually. You can Strike the adjacent creature with your deity's favored weapon. If you are holy or unholy, the Strike gains that trait. If your Strike hits, all your allies gain a +2 circumstance bonus to the triggering saving throw (or a +3 circumstance bonus on a critical hit).

> [!danger] Effect: Divine Rebuttal

**Source:** `= this.source` (`= this.source-type`)
