---
type: action
source-type: "Remaster"
traits: ["[[Downtime]]", "[[Manipulate]]"]
cast: "Passive"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You're wearing or holding a [[Healer's Toolkit]]

You spend at least 8 hours caring for a diseased creature. Attempt a Medicine check against the disease's DC. After you attempt to Treat a Disease for a creature, you can't try again until after that creature's next save against the disease.
- **Critical Success** You grant the creature a +4 circumstance bonus to its next saving throw against the disease.
- **Success** You grant the creature a +2 circumstance bonus to its next saving throw against the disease.
- **Critical Failure** Your efforts cause the creature to take a −2 circumstance penalty to its next save against the disease.

> [!danger] Effect: Treat Disease

**Source:** `= this.source` (`= this.source-type`)
