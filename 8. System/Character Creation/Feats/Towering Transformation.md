---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Barbarian]]", "[[Druid]]", "[[Emotion]]", "[[Fear]]", "[[Mental]]", "[[Rage]]", "[[Visual]]"]
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** Your size increases due to a polymorph effect.

The physical growth of your transformation is a spectacle that shakes foes to their core. Each enemy smaller than your new size within 30 feet of you must attempt a [[Will]] save against your class DC or spell DC, whichever is higher.
- **Success** The creature is unaffected.
- **Failure** The creature becomes [[Frightened]] 1.
- **Critical Failure** The creature becomes [[Frightened]] 2, and you can push it up to 10 feet from you. This is forced movement.

**Source:** `= this.source` (`= this.source-type`)
