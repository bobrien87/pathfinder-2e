---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Eternal Legend|Eternal Legend]]"
source-type: "Remaster"
level: "16"
traits: ["[[Mythic]]"]
prerequisites: "Eternal Legend Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You pounce toward an enemy and then barrel them over with one fluid movement, ending this maneuver with an attack that may catch them off-balance. [[Leap]] horizontally toward an enemy you can see; treat your Speed as 30 feet or more for this Leap if it is less than 30 feet. If you end this movement adjacent to that enemy, attempt an Acrobatics check to [[Tumble Through]] that enemy's space. On a success, the target is also knocked [[Prone]]. You then Strike that same enemy. If the target has been knocked prone, you can spend 1 Mythic Point as part of this Strike to make it at mythic proficiency.

**Source:** `= this.source` (`= this.source-type`)
