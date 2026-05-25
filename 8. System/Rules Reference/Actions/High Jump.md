---
type: action
source-type: "Remaster"
traits: ["[[Move]]"]
cast: "`pf2:2`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You Stride, then attempt a DC 30 Athletics check to jump vertically. If you didn't Stride at least 10 feet, you automatically fail. This DC might be increased or decreased due to the situation, as determined by the GM.
- **Critical Success** You [[Leap]] up to 8 feet vertically and 10 feet horizontally.
- **Success** You Leap up to 5 feet vertically and 5 feet horizontally.
- **Failure** You Leap normally.
- **Critical Failure** You fall [[Prone]] in your space.

**Source:** `= this.source` (`= this.source-type`)
