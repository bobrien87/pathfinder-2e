---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Overflow]]", "[[Primal]]", "[[Water]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Booming, crashing walls of water, enough to fill a harbor, smash out ahead of you, overwhelming all in their path. The waves move forward in your choice of a @Template[cone|distance:60] or @Template[line|distance:120]. If you're in water, you can increase these waves to a @Template[cone|distance:90] or @Template[line|distance:180]. Each creature in the area takes @Damage[10d10[bludgeoning]|options:area-damage] damage with a [[Reflex]] save against your class DC. A creature that fails its save is pushed 20 feet (or 40 feet on a critical failure). Any unattended object of 1 Bulk or less in the area is pushed to the far edge of the area. The sheer mass of water extinguishes all non-magical flames in the area.

As the wave crashes down, you can catch it to your destination. After the impulse deals damage, you can Swim in a straight line to any point in its area before the water disappears.

**Source:** `= this.source` (`= this.source-type`)
