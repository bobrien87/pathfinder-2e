---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Pure Legion Enforcer|Pure Legion Enforcer]]"
source-type: "Remaster"
level: "20"
traits: ["[[Archetype]]"]
prerequisites: "Pure Legion Enforcer Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You made yourself into a paragon of mortality and prove that deities aren't needed to achieve greatness. Choose a skill you have master proficiency in. You become legendary in that skill. In addition, you gain a skill feat of your choice for that skill. The first time each day that you succeed at a skill check with that skill, you gain a +3 status bonus to your next skill check of any skill within the next hour.

**Source:** `= this.source` (`= this.source-type`)
