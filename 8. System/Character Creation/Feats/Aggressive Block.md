---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Fighter]]", "[[Guardian]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You use the Shield Block reaction, and the opponent that triggered Shield Block is adjacent to you and is your size or smaller.

You push back as you block, knocking your foe away or off balance. You use your shield to push the triggering creature, either automatically Shoving it 5 feet or causing it to become [[Off Guard]] until the start of your next turn. The triggering creature chooses whether to be moved or become off-guard. If it chooses to be moved, you choose the direction. If the [[Shove]] would cause it to hit a solid object, enter a square of difficult terrain, or enter another creature's space, it must become off-guard instead of being moved.

**Source:** `= this.source` (`= this.source-type`)
