---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Earth]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The earth parts before you, letting you swim through it. You gain a burrow Speed equal to your land Speed and can immediately Burrow once. You don't gain the ability to breathe while in the earth, so you must hold your breath. The impulse ends at the end of your next turn, but you can Sustain it up to 1 minute. If you're inside the earth when the impulse ends, you immediately return to the surface directly above you, fall [[Prone]] when you reach the surface, and are [[Slowed]] 1 until the end of your next turn.

**Level (14th)** You can burrow through rock and similar dense earthen matter, leaving no tunnels or signs of your passing.

**Source:** `= this.source` (`= this.source-type`)
