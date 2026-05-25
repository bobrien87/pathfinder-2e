---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Beastmaster|Beastmaster]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Concentrate]]", "[[Primal]]"]
prerequisites: "Beastmaster Dedication, Call Companion"
frequency: "once per turn"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per turn

You quickly call in a primal projection of a non-active companion to provide the companion's support benefit. The projection arrives in an unoccupied square of your choice within 30 feet of you, grants you its support benefit, and then disappears on your next turn. The projection has the same AC and saving throw modifiers as the real companion, and if it would take any damage before your next turn, it disappears and the support benefit ends immediately.

**Source:** `= this.source` (`= this.source-type`)
