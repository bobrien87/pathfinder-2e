---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Secret]]"]
cast: "Passive"
source: "Pathfinder GM Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You watch or study an NPC to learn more about that NPC's preferences. Attempt a Perception check or an appropriate skill check determined by the GM. The DC is found in the NPC's influence stat block.
- **Critical Success** Choose two of the options detailed in Success below; you can choose the same option twice to learn two pieces of information from the same category.
- **Success** Choose one of the following: You learn which skill that can Influence the NPC has the lowest DC (skipping any skills that you already know), one of the NPC's personal biases, one of the NPC's resistances, or one of the NPC's weaknesses.
- **Failure** You learn no information.
- **Critical Failure** Choose a piece of information to learn about, as success, but the information is incorrect.

**Source:** `= this.source` (`= this.source-type`)
