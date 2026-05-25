---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Beast Gunner|Beast Gunner]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Beast Gunner Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've unlocked the first secrets of beast guns, granting you your own pool of magical might through the amplifying power of their synergistic magic. You gain the [[basic spellcasting benefits]]. Each time you gain a spell slot of a new rank from this archetype, add a spell of the appropriate spell rank to your repertoire, either a common spell of your chosen tradition or another spell of that tradition you've learned or discovered.

**Source:** `= this.source` (`= this.source-type`)
