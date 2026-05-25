---
type: action
source-type: "Remaster"
traits: ["[[Downtime]]"]
cast: "Passive"
source: "Pathfinder GM Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You seek to procure or create disguises. Attempt a normal, hard, or very hard Crafting, Deception, Performance, or Society check.
- **Success** You procure or creates disguises, gaining 1 EP that can be used only to maintain a cover identity.
- **Failure** Your efforts result in an unusable disguise.

**Source:** `= this.source` (`= this.source-type`)
