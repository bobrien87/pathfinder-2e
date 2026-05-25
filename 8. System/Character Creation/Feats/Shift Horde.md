---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Necrologist|Necrologist]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Magical]]", "[[Manipulate]]"]
prerequisites: "Necrologist Dedication"
frequency: "once per round"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per round

**Requirements** Your horde is raised.

With a wave of your hand, your risen undead horde collapses and another one rises to take its place. You Sustain your horde, dispersing the current group of undead and replacing them with a different type of undead to which you have access.

**Source:** `= this.source` (`= this.source-type`)
