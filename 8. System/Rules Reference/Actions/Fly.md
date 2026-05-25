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

**Requirements** You have a fly Speed.

You move through the air up to your fly Speed. Moving upward (straight up or diagonally) uses the rules for moving through difficult terrain. You can move straight down 10 feet for every 5 feet of movement you spend. If you Fly to the ground, you don't take falling damage. You can use an action to Fly 0 feet to hover in place. If you're airborne at the end of your turn and didn't use a Fly action this round, you fall.

**Source:** `= this.source` (`= this.source-type`)
