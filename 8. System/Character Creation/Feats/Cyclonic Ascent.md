---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Air]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Whorls of wind surround your lower body, forming a cyclone that lifts you into the air. You gain a fly Speed equal to your land Speed or 30 feet, whichever is greater, for 10 minutes. Unlike with a normal fly Speed, you can move upward without treating it as difficult terrain. In addition, you can remain in the air at the end of your turn if you used an air impulse during that turn, even if you didn't use a Fly action that turn.

> [!danger] Effect: Cyclonic Ascent

**Level (14th)** You can target up to five additional creatures, each of which gains a fly Speed equal to its land Speed or 30 feet, whichever is greater. They don't gain the other benefits.

**Source:** `= this.source` (`= this.source-type`)
