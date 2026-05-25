---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Tripkee]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your jumping prowess is unmatched. You can [[Leap]] up to 30 feet in any direction without touching the ground and without requiring an Athletics check; when doing so, you must land on a space of solid ground within 30 feet of you, or else you fall after using your next action. You can exceed your normal Speed while Leaping.

**Special** If you have the Fantastic Leaps feat, the total distance you can Leap horizontally is 40 feet, and the total distance you can Leap vertically is 35 feet.

**Source:** `= this.source` (`= this.source-type`)
