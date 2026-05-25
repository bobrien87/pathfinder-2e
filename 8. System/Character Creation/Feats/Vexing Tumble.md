---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Bravado]]", "[[Swashbuckler]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You tumble around your foes, expertly avoiding their reactions. Stride up to half your Speed and roll an [[Acrobatics]] check. Compare the result to the Reflex DC of each enemy whose reach you began in or enter during the movement, in sequence.
- **Critical Success** This movement doesn't trigger reactions from the enemy, and the enemy is [[Off Guard]] to you until the end of your turn
- **Success** This movement doesn't trigger reactions from the enemy.
- **Critical Failure** Your movement immediately stops when you enter the creature's reach; if you began in the creature's reach, you don't move.

**Source:** `= this.source` (`= this.source-type`)
