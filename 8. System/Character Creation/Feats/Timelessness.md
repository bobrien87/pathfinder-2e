---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Timewracked|Timewracked]]"
source-type: "Remaster"
level: "20"
traits: ["[[Mythic]]"]
prerequisites: "Timewracked Dedication"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Time travelers are rare, but even among them your isolation from time is unique. As long as you remain timewracked, you do not age and cannot die of natural causes. You're immune to hostile spells and effects related to time or aging, as well as the slowed condition (except for when you gain the slowed condition through this mythic destiny). You reduce the DC of recovery checks by 1. Whenever you roll a flat check to end persistent damage, you roll twice and choose your desired result; this is a fortune effect.

In addition, your intimate knowledge of the flow of time gives you a measure of influence over the attempt of another to manipulate it. Whenever an enemy creature that you are aware of and who is within 60 feet of you gains the [[Quickened]] condition, you gain the quickened condition for 1 round. The actions available to you from the acquired condition are the same as those granted by the ability that quickens your enemy.

**Source:** `= this.source` (`= this.source-type`)
