---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Fire]]", "[[Impulse]]", "[[Kineticist]]", "[[Manipulate]]", "[[Overflow]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Flames rise and shape to your will, forming a wall or dome of your design. You create a [[Wall of Fire]] within 120 feet. In addition to the normal choices, you can make the wall up to 10 feet long and 60 feet high. The wall lasts until the end of your next turn, but you can Sustain it up to 1 minute.

**Level (+3)** The damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
