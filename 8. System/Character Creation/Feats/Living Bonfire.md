---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Composite]]", "[[Fire]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]", "[[Wood]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Roots and branches of living wood writhe in elemental fire at your command, forming a bonfire fearsome enough to scare off predators in the night. You conjure a bonfire in an unoccupied @Template[square|distance:10]{10-foot-square} space within 30 feet. The bonfire burns for 10 hours, providing all the benefits of a normal campfire. If you use this impulse again, any previous one ends.

When you make a wood ranged Elemental Blast, you can have it come from the bonfire instead of you, flinging burning logs. This blast deals an additional @Damage[(floor((@actor.level -4)/5)+1)d6[fire]] damage. Each time you do this, the size of the bonfire is reduced by one 5-foot square. If all the squares are removed, the impulse ends.

**Level (+5)** The fire damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
