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

The moon has always been connected to the tides, and now you can grasp that connection. You can create massive amounts of water and control these tides, subverting even the moon's sovereignty over the oceans and seas. Choose an area @Template[square|distance:50]{50 feet long by 50 feet wide} within 500 feet, and choose two different effects from the options provided below. The effects take place in the listed order.

- **Flood** You create a pool of pure, clean water in the area, which coalesces from ambient moisture. This water must be created on a surface-not in air-and flows normally.

- **Control** You tug on the moon to raise or lower the level of bodies of water in the area by 10 feet. If you control a portion of a larger body of water, the water then equalizes normally.

- **Modulate** With a wave of your hand, you create or smooth ripples, making all bodies of water in the area either calm or turbulent. Making it calm turns difficult terrain or greater difficult terrain to calm water, and making it turbulent turns calm water into difficult terrain.

- **Slow** By exercising your rightful control over all water, each creature with the water trait in the area must succeed at a [[Fortitude]] save against your class DC or be [[Slowed]] 1 (or [[Slowed]] 2 on a critical failure).

Flood and control are permanent and non-magical. Modulate and slow last until the end of your next turn, but you can Sustain the impulse to continue them.

**Source:** `= this.source` (`= this.source-type`)
