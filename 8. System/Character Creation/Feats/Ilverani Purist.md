---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Twilight Speaker|Twilight Speaker]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Twilight Speaker Dedication"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

All twilight speakers are trained to resist the alluring customs of younger peoples, but you have made it your mandate to keep the Ilverani way unchanged. Such dedication has given you a trained eye for subtlety and deception. When you attempt to [[Sense the Motive]] of a non-elf humanoid creature and you roll a critical failure, you fail instead.

**Source:** `= this.source` (`= this.source-type`)
