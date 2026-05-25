---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Knight Reclaimant|Knight Reclaimant]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]"]
prerequisites: "Reaper of Repose"
source: "Pathfinder Claws of the Tyrant"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You use your imposing demeanor to set up the undead for defeat. Make a Strike against an undead creature using a weapon with which you have master proficiency. If you hit, all Strikes against that creature gain the benefits of [[Reaper of Repose]] for 1 round.

**Source:** `= this.source` (`= this.source-type`)
