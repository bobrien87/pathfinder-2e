---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Beast Lord|Beast Lord]]"
source-type: "Remaster"
level: "16"
traits: ["[[Mythic]]"]
prerequisites: "Beast Lord Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You and your companion are within 15 feet of each other, and a foe successfully Strikes your united companion.

You can protect your companion from danger with a well-timed attack. You can immediately Stride toward the triggering enemy and can make a Strike against them if they would be in the first range increment of your ranged weapon or within your melee reach. If this Strike is successful, reduce the damage to your companion by your level, or twice your level if the Strike was a critical success.

**Source:** `= this.source` (`= this.source-type`)
