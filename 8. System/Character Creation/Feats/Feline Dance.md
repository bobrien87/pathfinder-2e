---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Clawdancer|Clawdancer]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Fortune]]"]
prerequisites: "Clawdancer Dedication"
frequency: "once per PT1H"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** catfolk ancestry

**Frequency** once per hour

**Trigger** You attempt a basic Reflex save.

**Requirements** You're in either claw stance or talon stance.

You fluidly move between stances in the process of dodging. Roll the save twice and take the higher result. If you were in claw stance, you shift to talon stance, and vice versa.

**Source:** `= this.source` (`= this.source-type`)
