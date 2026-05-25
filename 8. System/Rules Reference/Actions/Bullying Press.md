---
type: action
source-type: "Remaster"
traits: ["[[Flourish]]"]
cast: "`pf2:r`"
source: "Pathfinder GM Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You attempt a melee Strike against your opponent, but haven't rolled yet.

**Requirements** You're in a duel, you're trained in Intimidation, and you rolled an Intimidation check for initiative this round.

If you hit, your opponent becomes [[Frightened]] 1. If your opponent is using Perception for initiative when this ability is used, they become [[Frightened]] 2 instead.

**Source:** `= this.source` (`= this.source-type`)
