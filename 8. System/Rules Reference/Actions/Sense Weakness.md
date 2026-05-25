---
type: action
source-type: "Remaster"
cast: "`pf2:r`"
source: "Pathfinder GM Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You attempt a melee Strike against your opponent, but haven't rolled yet.

**Requirements** You're in a duel, you're trained in Perception, and you rolled a Perception check for initiative this round.

You pick a precise moment to attack, giving you an edge. Your opponent is [[Off Guard]] against the attack. If your opponent is using Deception for initiative when this ability is used, they are instead off-guard until the start of their next turn.

**Source:** `= this.source` (`= this.source-type`)
