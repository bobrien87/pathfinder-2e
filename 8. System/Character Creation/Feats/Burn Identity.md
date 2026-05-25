---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Twilight Talon|Twilight Talon]]"
source-type: "Remaster"
level: "18"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Occult]]", "[[Teleportation]]"]
prerequisites: "Twilight Talon Dedication"
frequency: "once per P1W"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per week

You transport yourself up to 1 mile, as a 5th-rank translocate spell. Everyone who has seen you in the last 24 hours must succeed at a [[Will]] save against your class DC or spell DC, whichever is higher, or forget your physical appearance as though affected by a 6th-rank [[Rewrite Memory]] spell. You can choose to exempt any number of creatures from this effect. You can instead Burn Identity as an activity that takes 10 minutes. If you do, instead of the effects of [[Translocate]], you can instantly teleport yourself and up to four targets touched (either willing creatures or objects roughly the size of a creature) to the nearest border of Andoran, in addition to its other effects.

**Source:** `= this.source` (`= this.source-type`)
