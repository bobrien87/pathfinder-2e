---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Warshard Warrior|Warshard Warrior]]"
source-type: "Remaster"
level: "14"
traits: ["[[Mythic]]"]
prerequisites: "Warshard Warrior Dedication"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you choose a warshard weapon during daily preparations, you can transform the material it's composed of so that the weapon is made of a precious material (like adamantine, dawnsilver, or cold iron). The material and quality of the material you select must be of a level equal to or less than your character level. You can transmute the weapon into a standard-grade item of that material only if the weapon is at least level 9. You can transmute the weapon into high-grade item of that material only if the weapon is at least level 15.

**Source:** `= this.source` (`= this.source-type`)
