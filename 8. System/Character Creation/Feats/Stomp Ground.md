---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Guardian]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You bring your booted foot down on the ground with enough force to rattle your foes. Each creature in a @Template[type:emanation|distance:5] must attempt a [[Reflex]] save saving throw against your class DC.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Off Guard]] until the end of your turn.
- **Failure** The creature is knocked [[Prone]].
- **Critical Failure** The creature is knocked prone and takes @Damage[1d6[bludgeoning]|options:area-damage] damage from the fall.

**Source:** `= this.source` (`= this.source-type`)
