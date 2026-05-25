---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Dwarf]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You are from Dongun Hold or Alkenstar.

Your family's traditions of defending against Geb's undead have granted you a sixth sense for detecting spirits, haunts, and other restless dead, no matter their form or the strength of their presence. You gain a +2 circumstance bonus to Perception checks to [[Sense Motive]] when trying to determine if a creature is possessed or under the influence of an effect that would make them controlled, a +2 circumstance bonus to Perception checks made to see through disguises worn by undead, and a +2 circumstance bonus when using the [[Seek]] action to find [[Hidden]] or undetected haunts or undead within 30 feet of you.

If you aren't using the [[Seek]] action or searching, the GM automatically rolls a secret check for you to notice haunts or undead within 30 feet anyway. This check doesn't gain the usual +2 circumstance bonus, and instead takes a –2 circumstance penalty.

**Source:** `= this.source` (`= this.source-type`)
