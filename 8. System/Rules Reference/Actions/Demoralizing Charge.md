---
type: action
source-type: "Remaster"
traits: ["[[Brandish]]", "[[Commander]]", "[[Tactic]]"]
cast: "`pf2:2`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Your team's coordinated assault strikes fear into your enemies' hearts. Signal up to two squadmates within the aura of your commander's banner; as a free action, those squadmates can immediately Stride toward an enemy they are observing.

If they end this movement adjacent to an enemy, they can attempt to Strike that enemy as a reaction. For each of these Strikes that are successful, the target enemy must succeed at a [[Will]] save against your class DC or become [[Frightened]] 1 ([[Frightened]] 2 on a critical failure); this is an emotion, fear, and mental effect.

If both Strikes target the same enemy, that enemy attempts the save only once after the final attack and takes a –1 circumstance penalty to their Will save to resist this effect (this penalty increases to –2 if both Strikes are successful or to –3 if both Strikes are successful and either is a critical hit.)

> [!danger] Effect: Demoralizing Charge

**Source:** `= this.source` (`= this.source-type`)
