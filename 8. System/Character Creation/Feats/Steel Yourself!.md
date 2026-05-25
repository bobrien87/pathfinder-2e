---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Marshal|Marshal]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Emotion]]", "[[Mental]]"]
prerequisites: "Marshal Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You encourage an ally to toughen up, giving them a fighting chance. Choose one ally in your marshal's aura. The ally gains temporary Hit Points equal to your Charisma modifier and a +2 circumstance bonus to Fortitude saves. Both benefits last until the start of your next turn.

> [!danger] Effect: Steel Yourself!

**Source:** `= this.source` (`= this.source-type`)
