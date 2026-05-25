---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Hellknight|Hellknight]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Hellknight Dedication"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You gain the lesser order benefit of a Hellknight order other than the one to which you belong. This represents your time spent training with members of that order to learn their techniques and teachings. If you aren't in good standing with a given order, you can't receive their training.

**Special** You can select this feat multiple times, gaining the lesser order benefit from a different order each time by training with members of that order.

**Source:** `= this.source` (`= this.source-type`)
