---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Broken Chain|Broken Chain]]"
source-type: "Remaster"
level: "18"
traits: ["[[Mythic]]"]
prerequisites: "Broken Chain Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have tied yourself so absolutely to the cause of liberty that your very existence is an act of rebellion. You ignore any mental effects without the fear trait that would rob you of your agency (for example, on a failed save against [[Charm]] you would still be able to take hostile actions, and against [[Laughing Fit]] you would still be able to take reactions but would remain [[Slowed]], but on a critical failure against [[Fear]] you would still be [[Fleeing]] because it's a fear effect).

Additionally, you are immune to effects that would imprison your soul (such as [[Seize Soul]], or a [[Final Blade]]).

**Source:** `= this.source` (`= this.source-type`)
