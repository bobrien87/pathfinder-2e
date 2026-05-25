---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Ranger]]"]
prerequisites: "animal feature warden spell"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You tap into the primal strength of your animal feature. When you gain a claw or jaws attack from animal feature, you can choose a weapon you're carrying and apply all runes from that weapon (if they're applicable) to that unarmed attack. This replaces any runes the unarmed attacks would normally have from other sources, like handwraps of mighty blows. In addition, when you critically hit with a claw or jaws attack from animal feature, you deal 1d6 persistent,bleed damage.

**Source:** `= this.source` (`= this.source-type`)
