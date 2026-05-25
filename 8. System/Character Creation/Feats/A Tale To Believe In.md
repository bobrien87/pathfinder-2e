---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Field Propagandist|Field Propagandist]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Concentrate]]", "[[Linguistic]]", "[[Mental]]"]
prerequisites: "Field Propagandist Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You recite a tale of prowess that rewrites the combat unfolding around you. You can attempt a counteract check against a mental effect that's currently affecting an ally within 30 feet, using Deception for the counteract check and half your level as the counteract rank.

**Source:** `= this.source` (`= this.source-type`)
