---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Earth]]", "[[Impulse]]", "[[Kineticist]]", "[[Manipulate]]", "[[Overflow]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Drawing on your connection to the Plane of Earth, you form a wall of rock and earth. This has the effect of [[Wall of Stone]], but the wall's maximum length is 40 feet. The wall lasts until the end of your next turn, but you can Sustain it up to 1 minute.

**Level (+4)** The maximum length of the wall increases by 10 feet, and the Hit Points of each section increase by 5.

**Source:** `= this.source` (`= this.source-type`)
