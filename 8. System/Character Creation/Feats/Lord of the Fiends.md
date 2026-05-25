---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Archfiend|Archfiend]]"
source-type: "Remaster"
level: "14"
traits: ["[[Mythic]]"]
prerequisites: "Archfiend Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You consider every fiend a future subject and can assess them at a glance. Spend a Mythic Point. Attempt a check at mythic proficiency to Recall Knowledge about every fiend you can see. For the next hour, whenever you roll a success on a Deception, Diplomacy, or Intimidation check against a fiend, you get a critical success instead.

**Source:** `= this.source` (`= this.source-type`)
