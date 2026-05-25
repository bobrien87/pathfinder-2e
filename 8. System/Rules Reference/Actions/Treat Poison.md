---
type: action
source-type: "Remaster"
traits: ["[[Manipulate]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You're wearing or holding a [[Healer's Toolkit]]

You treat a patient to prevent the spread of poison. Attempt a Medicine check against the poison's DC. After you attempt to Treat a Poison for a creature, you can't try again until after the next time that creature attempts a save against the poison.
- **Critical Success** You grant the creature a +4 circumstance bonus to its next saving throw against the poison.
- **Success** You grant the creature a +2 circumstance bonus to its next saving throw against the poison.
- **Critical Failure** Your efforts cause the creature to take a −2 circumstance penalty to its next save against the poison.

> [!danger] Effect: Treat Poison

**Source:** `= this.source` (`= this.source-type`)
