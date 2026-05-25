---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Godling|Godling]]"
source-type: "Remaster"
level: "14"
traits: ["[[Concentrate]]", "[[Mental]]", "[[Mythic]]"]
prerequisites: "Godling Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You open your senses so the prayers of mortals can better reach your ears. You gain a +1 status bonus to checks to [[Sense Motive]], but only when attempting to ascertain hopes, prayers, wishes, and other strongly held desires of the target. You gain an even greater sense of your hierophant's prayers, which grants you a constant status as a constant divine spell targeting your hierophant. The spell has unlimited duration and functions at any range, included across planar boundaries, and counteracting the spell merely suppresses it until your next daily preparations, though it automatically ends if the creature stops being your hierophant.

You gain the ability to cast [[Breath of Life]] once per day as a 5th-rank divine innate spell. You can cast this spell only on your hierophant, and the spell has unlimited range (your status spell typically alerting to you to when your hierophant would die).

**Source:** `= this.source` (`= this.source-type`)
