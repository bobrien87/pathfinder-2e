---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Runelord|Runelord]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]"]
prerequisites: "Runelord Dedication, Counterspell"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your deep connection to a specific sin allows you to easily negate spells that sin opposes. Instead of being able to counter a foe's spell with Counterspell only if you have the same spell prepared, you can Counterspell it with any of your curriculum spells if the spell cast would violate your sin's anathema.

**Source:** `= this.source` (`= this.source-type`)
