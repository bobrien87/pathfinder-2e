---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Eternal Legend|Eternal Legend]]"
source-type: "Remaster"
level: "18"
traits: ["[[Emotion]]", "[[Fear]]", "[[Mental]]", "[[Mythic]]", "[[Visual]]"]
prerequisites: "Eternal Legend Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Raising your weapon or fist aloft, you begin to gleam with dazzling radiance. You fulminate with power and glory, making it clear to all who see you that your legend is real and possibly even greater than purported. Spend a Mythic Point. All enemies who can see you must succeed at a [[Will]] save saving throw against your class DC or become [[Frightened]] 3 ([[Frightened]] 4 on a critical failure). You and any ally who can see you may choose to Strike or Stride as a free action. Any of these Strikes are made at mythic proficiency.

**Source:** `= this.source` (`= this.source-type`)
