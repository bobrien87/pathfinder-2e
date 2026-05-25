---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Stalwart Defender|Stalwart Defender]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Stalwart Song"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You know story after story of unyielding, valiant dwarven heroes whose minds were bulwarks against fear and confusion. You can use [[Stalwart Song]] when attempting a saving throw against any mental effect, and if you fail the saving throw, you gain resistance to mental damage against any resulting effect equal to half your level.

**Source:** `= this.source` (`= this.source-type`)
