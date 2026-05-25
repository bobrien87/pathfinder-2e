---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Guardian]]"]
prerequisites: "Shield Block"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You used [[Shield Block]] to prevent damage from an adjacent creature's attack.

As you absorb a blow from an enemy, you can use their attack's momentum against them. Attempt to [[Reposition]] the creature whose attack you used Shield Block against. You don't need to have a hand free to do so. You gain a +1 item bonus to the Athletics check if your shield is at least 4th level, a +2 item bonus if your shield is at least 10th level, and a +3 item bonus if your shield is at least 16th level.

**Source:** `= this.source` (`= this.source-type`)
