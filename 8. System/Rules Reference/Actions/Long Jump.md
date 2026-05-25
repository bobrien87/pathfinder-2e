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

You Stride, then attempt a DC 15 Athletics check to make a long jump in the direction you were Striding. If you didn't Stride at least 10 feet, you automatically fail your check. The GM might increase or decrease this DC depending on the situation.
- **Success** You [[Leap]] up to a distance equal to your check result rounded down to the nearest 5 feet. You can't jump farther than your land Speed.
- **Failure** You make a normal horizontal Leap.
- **Critical Failure** You make a normal horizontal Leap, then fall and land [[Prone]].

**Source:** `= this.source` (`= this.source-type`)
