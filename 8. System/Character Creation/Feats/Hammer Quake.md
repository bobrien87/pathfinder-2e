---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Mauler|Mauler]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Mauler Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a non-finesse melee weapon in two hands.

You smash the ground with your weapon, knocking nearby creatures to the ground. Choose a square within your reach, including your own space. If there's an enemy in the chosen square, you can Strike that enemy with your two-handed weapon. Regardless of whether you attempted a Strike, you then attempt to [[Trip]] every enemy in the chosen square plus each square adjacent to that square, ignoring Trip's requirement that you have a hand free.

Hammer Quake counts as three attacks toward your multiple attack penalty, but the penalty doesn't increase until after you've made the Strike, if any, and all the Trip attempts.

**Source:** `= this.source` (`= this.source-type`)
