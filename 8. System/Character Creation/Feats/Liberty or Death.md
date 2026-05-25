---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Broken Chain|Broken Chain]]"
source-type: "Remaster"
level: "18"
traits: ["[[Death]]", "[[Incapacitation]]", "[[Mythic]]"]
prerequisites: "Broken Chain Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** A creature has been the target of your [[Ultimatum of Liberation]] for at least 1 minute

You have given a despot enough time to think, and now is the time for them to forfeit their control or die. Spend a Mythic Point and make a Strike at mythic proficiency against the required creature. If you succeed and deal damage, the target must succeed on a [[Fortitude]] save against your class DC or spell DC (whichever is higher) or die. If the target succeeds, they are immune to this ability for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
