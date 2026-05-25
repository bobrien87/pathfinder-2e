---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Archfiend|Archfiend]]"
source-type: "Remaster"
level: "14"
traits: ["[[Concentrate]]", "[[Mythic]]"]
prerequisites: "Archfiend Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With a thought, the passion of your fiendish desires becomes evident in your eyes and posture. For the next minute, you gain a +2 circumstance bonus to Deception, Diplomacy, and Intimidation skill checks. In addition, you gain a +2 circumstance bonus to counteract checks. At 18th level, these circumstance bonuses increase to +3.

**Source:** `= this.source` (`= this.source-type`)
