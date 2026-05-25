---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Nidalese Horselord|Nidalese Horselord]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Nidalese Horselord Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're riding your horse and wielding a melee weapon.

You charge into the fray on horseback, and those that lurk in the shadows will feel your wrath. You Command an Animal to have your mount Stride up to double its Speed. You can make a melee Strike at up to two enemies that are within your reach at any point during your mount's movement. Both attacks count toward your multiple attack penalty, but the penalty doesn't increase until after you've made both of them.

Each Strike that hits a creature in dim light or darkness deals an additional 3d6 damage of the same type as the Strike. This additional damage increases to 4d6 at 15th level and to 5d6 at 18th level.

**Source:** `= this.source` (`= this.source-type`)
