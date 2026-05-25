---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Fire]]", "[[Impulse]]", "[[Kineticist]]", "[[Manipulate]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You mimic the motions of a beast of your devising, and it becomes real, with a flaming pelt and searing claws. It is Small and appears in an unoccupied space within 30 feet. You can sense from the crawling fire's space as well as your own, using your senses. When you use a fire impulse, you can have it originate from the crawling fire instead of you (with the exception of impulses that affect your kinetic aura).

The creation lasts until the end of your next turn, but you can Sustain it up to 1 minute. Each time you Sustain it, you can have the crawling fire Stride up to 40 feet. The crawling fire can be attacked. It uses your statistics for defenses but is immune to fire. Any damage that would be dealt to the crawling fire is dealt to you instead, though you take damage only once from any ability that includes both you and the creation in the area of effect. If you use Crawling Fire again, any previous one ends.

**Level (8th)** The fire can be Small or Medium.

**Level (10th)** The fire can be Small, Medium, or Large.

**Level (14th)** The fire can be Small, Medium, Large, or Huge.

**Source:** `= this.source` (`= this.source-type`)
