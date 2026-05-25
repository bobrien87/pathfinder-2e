---
type: action
source-type: "Remaster"
traits: ["[[Move]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You Stride up to your Speed. During this movement, you can try to move through the space of one enemy. Attempt an Acrobatics check against the enemy's Reflex DC as soon as you try to enter its space. You can Tumble Through using Climb, Fly, Swim, or another action instead of Stride in the appropriate environment.
- **Success** You move through the enemy's space, treating the squares in its space as difficult terrain (every 5 feet costs 10 feet of movement). If you don't have enough Speed to move all the way through its space, you get the same effect as a failure.
- **Failure** Your movement ends, and you trigger reactions as if you had moved out of the square you started in.

**Source:** `= this.source` (`= this.source-type`)
