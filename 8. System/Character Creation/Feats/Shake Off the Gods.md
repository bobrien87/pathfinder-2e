---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Pure Legion Enforcer|Pure Legion Enforcer]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Concentrate]]"]
prerequisites: "Pure Legion Enforcer Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're under an effect with the divine trait that required a saving throw.

Your trust in the Pure Legion rushes forth as you fight off the influence of a god. You can attempt a new saving throw against the required effect with a +2 status bonus to the save. You can't get a worse result than your original saving throw.

**Source:** `= this.source` (`= this.source-type`)
