---
type: action
source-type: "Remaster"
cast: "`pf2:2`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per hour

**Effect** Your familiar's mouth opens impossibly wide before your patron's grasping limb stretches forth from it at a creature within 30 feet, dealing 10d10 spirit damage with a [[Fortitude]] save against your spell DC. If the creature fails its save and takes damage, it is also [[Drained]] 2 (or [[Drained]] 4 on a critical failure) and you regain 1 Focus Point, up to your usual maximum, as your patron grants you additional magic in exchange for your gift of your opponent's spirit.

**Source:** `= this.source` (`= this.source-type`)
