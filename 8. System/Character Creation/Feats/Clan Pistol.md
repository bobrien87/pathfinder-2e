---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Dwarf]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You are from Dongun Hold or Alkenstar.

Raised in the ancient halls of Dongun Hold or the surrounding region, you display your lineage with a clan pistol, rather than a clan dagger. You get one clan pistol of your clan for free, as it was given to you at birth. This replaces your clan dagger. Selling this pistol is a terrible taboo and earns you the disdain of other dwarves. You are trained with the clan pistol. In addition, when your clan pistol is visible, you gain a +1 circumstance bonus on checks to [[Gather Information]] or [[Make an Impression]] when interacting with citizens of Alkenstar, Dongun Hold, or their allies.

**Source:** `= this.source` (`= this.source-type`)
