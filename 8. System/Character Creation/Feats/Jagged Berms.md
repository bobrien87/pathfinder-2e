---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Composite]]", "[[Earth]]", "[[Impulse]]", "[[Kineticist]]", "[[Overflow]]", "[[Primal]]", "[[Wood]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You conjure up to six cube-shaped mounds of packed earth. Each appears in an unoccupied square within 120 feet, fills its square, and provides cover. A mound has AC 10, Hardness 10, and 20 HP, and is immune to critical hits and precision damage. If destroyed, a mound becomes difficult terrain. The mounds last for an unlimited duration, but if you use the impulse again, any previous one ends.

Sharpened wooden stakes protrude from each mound into adjacent squares. They can project from any of its sides; you choose which sides for each mound. For each square of wooden stakes a creature enters, that creature takes @Damage[(floor((@actor.level -6)/2)+2)d6[piercing]] damage. Destroying a mound also destroys its stakes.

**Level (+2)** The HP of each section of the wall increases by 10, and the piercing damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
