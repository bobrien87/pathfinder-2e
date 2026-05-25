---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Heroic Scion|Heroic Scion]]"
source-type: "Remaster"
level: "14"
traits: ["[[Exploration]]", "[[Mythic]]"]
prerequisites: "Heroic Scion Dedication"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You adapt quickly to new settings and terrains. When you make your daily preparations in a region you've never visited before (such as a city, geographical region, or small demiplane, but not in a dungeon, structure, or other location that focuses on encounter mode play), you spend part of that time introspectively digging into the memories of your past life to get a feel for the adventure that awaits.

Choose one of the following Exploration activities: [[Avoid Notice]], [[Defend]], [[Investigate]], [[Scout]], or [[Search]]. You perform that exploration activity at full speed rather than at half speed, and any skill check you attempt as a result of this Exploration activity is made at mythic proficiency.

These benefits end as soon as you enter a new region, as determined by the GM.

**Source:** `= this.source` (`= this.source-type`)
