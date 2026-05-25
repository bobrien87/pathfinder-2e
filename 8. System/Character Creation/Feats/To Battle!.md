---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Marshal|Marshal]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Flourish]]"]
prerequisites: "Marshal Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With a resounding cry, you rally your ally to take the offensive. Choose one ally in your marshal's aura who has a reaction available. If you spend 1 action, that ally can use their reaction to immediately Stride. If you spend 2 actions, that ally can use their reaction to immediately Strike.

**Source:** `= this.source` (`= this.source-type`)
