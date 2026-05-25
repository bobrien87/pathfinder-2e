---
type: action
source-type: "Remaster"
cast: "`pf2:2`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per 10 minutes

**Effect** Your familiar's spirit exits its body, leaving its empty shell behind, before flying at an enemy within 20 feet and dealing @Damage[(6+max(0,(ceil((@actor.level -8)/2)*2)))d6[spirit]] damage, with a [[Will]] save against your spell DC. If the familiar dealt damage, it then flies to an ally within 30 feet of the enemy, restoring Hit Points equal to half the damage dealt. Your familiar then re-forms in its original square. At 9th level, and every 2 levels thereafter, the attack deals an additional 2d6 damage.

**Source:** `= this.source` (`= this.source-type`)
