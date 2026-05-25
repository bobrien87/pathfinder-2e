---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Steel Falcon|Steel Falcon]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Auditory]]", "[[Emotion]]", "[[Incapacitation]]", "[[Linguistic]]", "[[Mental]]"]
prerequisites: "Steel Falcon Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're benefiting from the bonuses of Size Up.

You have an eerie ability to guess the next move of creatures you've Sized Up. You inform a foe that you know exactly what it'll do next, momentarily shocking it into inaction. If your focus from Size Up is within 30 feet of you, your focus must succeed at a [[Will]] save against your class DC or spell DC, whichever is higher, or be [[Stunned]] 1 (or [[Stunned]] 2 on a critical failure).

Regardless of the result, the target becomes temporarily immune to your Uncanny Prediction for 1 hour.

**Source:** `= this.source` (`= this.source-type`)
