---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Cavalier|Cavalier]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Cavalier Dedication, expert in Acrobatics or Athletics"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You Command an Animal to order your mount to Stride (or to Burrow, Climb, Fly, or Swim if it has the corresponding movement type). At any point during this movement, it must move adjacent to you. As it passes you, you [[Mount]] your mount. You can increase the number of actions you use with Dashing Pickup to 2 to make your mount Stride twice, or to 3 to make your mount Stride four times; you must use enough actions to ensure your mount is able to move adjacent to you at some point during this movement, and you cannot use this activity if it is not possible for your mount to do so.

**Source:** `= this.source` (`= this.source-type`)
