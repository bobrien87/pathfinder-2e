---
type: action
source-type: "Remaster"
traits: ["[[Misfortune]]"]
cast: "`pf2:r`"
source: "Pathfinder GM Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** An opponent hits, but does not critically hit you, with a melee Strike.

**Requirements** You're in a duel, you're trained in Deception, and you rolled a Deception check for initiative this round.

You draw your enemy in and pull away at the last moment. The triggering opponent must roll again and take the second result. If your opponent is using Intimidation for initiative when this ability is used, they also take a -2 circumstance penalty to the second attack roll.

**Source:** `= this.source` (`= this.source-type`)
