---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Morph]]", "[[Primal]]", "[[Wood]]"]
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You adapt a creature to live among the trees, improving its ability to climb, balance, and leap. Target a willing creature within 30 feet. For 10 minutes, it gains a climb Speed equal to its Speed and a +1 circumstance bonus to Acrobatics checks to [[Balance]] and Athletics checks to [[Long Jump]] and [[High Jump]]. When it Leaps, it increases the distance it can [[Leap]] horizontally by 5 feet and vertically by 2 feet. If you use Born to the Trees again, any existing one ends.

> [!danger] Effect: Born to the Trees

**Level (6th)** You can target up to 5 willing creatures.

**Source:** `= this.source` (`= this.source-type`)
