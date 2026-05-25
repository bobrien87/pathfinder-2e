---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Viking|Viking]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Viking Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You make a ranged Strike with a thrown weapon you already have in your hand, Stride, and then [[Interact]] to draw another weapon.

**Special** If you are [[Raging]], and end the Stride adjacent to an enemy, that enemy is [[Off Guard]] against the next Strike you make against it with the weapon you drew before the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
