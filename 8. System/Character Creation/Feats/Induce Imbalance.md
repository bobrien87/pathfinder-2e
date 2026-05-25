---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Five Breath Vanguard|Five Breath Vanguard]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Five-Breath Vanguard Dedication"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're in an elemental stance.

Your blows can disrupt the delicate balance of elemental energies that keep a body in good health. Strike the target using the unarmed attack associated with your current elemental stance. On a success, the target must attempt a [[Fortitude]] save against your class DC. On a failure, the target is [[Clumsy]] 2 until the end of your next turn. On a critical failure, the target is [[Clumsy]] 3 for 1 minute. Elementals take a –2 circumstance penalty to their save.

**Source:** `= this.source` (`= this.source-type`)
