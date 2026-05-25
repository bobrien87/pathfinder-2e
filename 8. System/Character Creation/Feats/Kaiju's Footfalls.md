---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Kobold]]"]
prerequisites: "mightyfall kobold heritage"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You channel the might and mass of a kaiju. You can cast [[Enlarge]] as an innate primal spell twice per day, targeting yourself. The first time each turn you [[High Jump]], [[Leap]], or [[Long Jump]] while affected by this spell, creatures of your size or smaller adjacent to where you land must attempt a [[Reflex]] save against your class DC or spell DC, whichever is higher.
- **Failure** The creature is knocked [[Prone]].
- **Critical Failure** The creature is knocked prone and takes @Damage[2d6[bludgeoning]|options:area-damage] damage.

At 17th level, you can choose to heighten this innate *enlarge* spell to 4th rank.

**Source:** `= this.source` (`= this.source-type`)
