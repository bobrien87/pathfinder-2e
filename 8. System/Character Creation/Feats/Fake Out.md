---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Gunslinger]]", "[[Visual]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An ally is about to use an action that requires an attack roll, targeting a creature within your weapon's first range increment.

**Requirements** You're wielding a loaded firearm or crossbow.

With a skilled flourish of your weapon, you force an enemy to acknowledge you as a threat. Make an attack roll to [[Aid]] the triggering attack. If you dealt damage to that enemy with the same weapon since the start of your last turn, you gain a +1 circumstance bonus to this roll.

**Source:** `= this.source` (`= this.source-type`)
