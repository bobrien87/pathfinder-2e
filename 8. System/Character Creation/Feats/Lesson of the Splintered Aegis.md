---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Iridian Choirmaster|Iridian Choirmaster]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Fortune]]"]
prerequisites: "Iridian Choirmaster Dedication"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your last action was a Strike that dealt damage to an enemy.

With your attack, you demonstrate to your student a hole in your enemy's defenses. Before the beginning of your next turn, your student can roll their next Strike or spell attack roll against that same enemy twice and take the better result.

> [!danger] Effect: Lesson of the Splintered Aegis

**Source:** `= this.source` (`= this.source-type`)
