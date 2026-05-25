---
type: action
source-type: "Remaster"
traits: ["[[Commander]]", "[[Tactic]]"]
cast: "`pf2:2`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per 10 minutes

You and your squad surge forward with a mighty roar. Signal all squadmates within the aura of your commander's banner. As a reaction, these squadmates can Stride up to twice their Speed directly toward any enemy they are observing.

Any creature within 10 feet of a squadmate once all movement from this tactic has been completed must attempt a [[Will]] save against your class DC with the following results. This is an emotion, fear, incapacitation, and mental effect.
- **Critical Success** No effect.
- **Success** The target is [[Frightened]] 1.
- **Failure** The target is [[Frightened]] 2.
- **Critical Failure** The target is [[Frightened]] 3 and [[Fleeing]] for 1 round.

**Source:** `= this.source` (`= this.source-type`)
