---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Kobold]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Through the lingering influence of your warren's patron, you've sprouted a small set of wings. While not suitable for full flight, these weak wings can help you jump further with a small flap. When Leaping horizontally, you move an additional 5 feet. This additional distance isn't cumulative with the increased [[Leap]] distance from the [[Powerful Leap]] feat. In addition, when you attempt a [[Long Jump]], you can jump a distance up to 10 feet farther than you normally would based on the result of your Athletics check, though you still can't jump farther than your Speed. You don't automatically fail your checks to [[High Jump]] or Long Jump if you don't Stride at least 10 feet first.

**Source:** `= this.source` (`= this.source-type`)
