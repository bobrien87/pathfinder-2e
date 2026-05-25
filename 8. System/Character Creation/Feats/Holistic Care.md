---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Medic|Medic]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "trained in Diplomacy, Treat Condition"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You provide emotional and spiritual care. Add [[Frightened]], [[Stupefied]], and [[Stunned]] to the list of conditions you can reduce with [[Treat Condition]]. If the stunned condition has a duration instead of a value, you can't use Treat Condition to reduce it.

**Source:** `= this.source` (`= this.source-type`)
