---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Cavalier|Cavalier]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Cavalier Dedication, trained in Nature"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You fall from a height of 15 feet or higher.

**Requirements** Your mount can reach your landing location with a single Stride.

As you fall, your mount dashes to your rescue. Your mount Strides up to its Speed, positioning itself below you. Rather than falling on your mount, you [[Mount]] your mount. Treat the triggering fall as if it were 15 feet shorter, and you don't land [[Prone]] (though both you and your mount both take damage from the fall based on what you would normally take for any remaining distance).

**Source:** `= this.source` (`= this.source-type`)
