---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Vigilante|Vigilante]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]", "[[Vigilante]]"]
prerequisites: "Startling Appearance"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your sudden appearance leaves your foe unable to respond. When you use Startling Appearance, if your foe's level is equal to or lower than yours, they are also [[Stunned]] 1 on a hit, or [[Stunned]] 2 on a critical hit.

**Source:** `= this.source` (`= this.source-type`)
