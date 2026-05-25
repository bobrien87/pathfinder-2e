---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Flourish]]", "[[Guardian]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wearing medium or heavy armor.

You charge into a group of enemies to send them flying. Stride up to your Speed. At the end of your movement, you can [[Shove]] up to three creatures within your reach. You don't need a hand free to do so. You attempt a separate Athletics check for each one; each attempt counts toward your multiple attack penalty, but the penalty doesn't increase until after you've made all the attempts. Regardless of your results, you can't Stride to follow any of the targets.

**Source:** `= this.source` (`= this.source-type`)
