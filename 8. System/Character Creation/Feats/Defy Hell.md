---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Hellbreaker|Hellbreaker]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Divine]]", "[[Stance]]"]
prerequisites: "Hellbreaker Dedication"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You aren't unholy.

Your devotion to your cause gives you endless strength and courage to withstand the enemy's attacks. As long as you're in this stance, you gain a +2 status bonus to saves against mental effects and can make [[Hellbreaker Strikes]].

**Source:** `= this.source` (`= this.source-type`)
