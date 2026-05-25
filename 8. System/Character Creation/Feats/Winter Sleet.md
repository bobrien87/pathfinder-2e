---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Cold]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]", "[[Stance]]", "[[Water]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Bone-chilling, swirling sleet surrounds you, cruel as deepest winter. Surfaces in your kinetic aura are coated in slippery ice. A creature that moves on the ice immediately falls unless it succeeds at an [[Acrobatics]] check or [[Reflex]] save against your impulse DC – 2. A creature that Steps or Crawls doesn't have to attempt a check or save. You're immune to this effect.

If a creature on the ice is critically hit by one of your water impulses or critically fails at a save against one, that creature is [[Slowed]] 1 until the end of its next turn.

**Source:** `= this.source` (`= this.source-type`)
