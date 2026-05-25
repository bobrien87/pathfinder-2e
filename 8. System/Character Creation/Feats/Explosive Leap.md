---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Fire]]", "[[Inventor]]", "[[Move]]", "[[Unstable]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You aim an explosion from your innovation downward to launch yourself into the air. You jump up to 30 feet in any direction without touching the ground. You must land on a space of solid ground, or else you fall after using your next action. As normal for effects where you fall after using your next action, you still fall at the end of your turn, even if you don't use any further actions that turn.

**Special** If your innovation is a minion, it can take this action rather than you.

**Source:** `= this.source` (`= this.source-type`)
