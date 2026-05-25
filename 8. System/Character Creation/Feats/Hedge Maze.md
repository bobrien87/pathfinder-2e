---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Overflow]]", "[[Plant]]", "[[Primal]]", "[[Wood]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You sculpt a manicured maze of hedges. Up to 10 hedges spring from the ground where you choose in a 30-foot-square area within 120 feet. Each is 10 feet long, 5 feet wide, and 15 feet tall. The hedges grant standard cover, are difficult terrain, and have a Climb DC of 15. They last until the end of your next turn, and you can Sustain the impulse up to 1 minute.

You can spend 10 minutes using this impulse as an exploration activity to instead create a cozy cabin with hedges for walls. It lasts for 12 hours, but ends if you use the impulse again.

**Source:** `= this.source` (`= this.source-type`)
