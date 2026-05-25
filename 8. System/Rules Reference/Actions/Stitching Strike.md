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

**Effect** Your familiar unravels into magical fibers that encompass an enemy within 30 feet and deal @Damage[(6+max(0,(ceil((@actor.level -8)/2)*2)))d6[slashing]] damage, with a [[Reflex]] save against your spell DC. On a failure, the target is also [[Immobilized]] for 1 round or until it [[Escapes]] against your spell DC. Your familiar then re-forms in its original square. At 9th level, and every 2 levels thereafter, the attack deals an additional 2d6 damage.

**Source:** `= this.source` (`= this.source-type`)
