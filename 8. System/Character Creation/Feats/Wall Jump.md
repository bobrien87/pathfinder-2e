---
type: feat
source-type: "Remaster"
level: "7"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "master in Athletics"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can use your momentum from a jump to propel yourself off a wall. If you're adjacent to a wall at the end of a jump (whether performing a [[High Jump]], [[Long Jump]], or [[Leap]]), you don't fall as long as your next action is another jump. Your previous jump gives you momentum, letting you use High Jump or Long Jump as a single action, but you don't get to Stride as part of the activity.

You can use Wall Jump only once in a turn, unless you're legendary in Athletics, in which case you can use it as many times as you can use consecutive jump actions in that turn.

**Source:** `= this.source` (`= this.source-type`)
