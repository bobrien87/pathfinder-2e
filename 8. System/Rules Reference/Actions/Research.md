---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Exploration]]"]
cast: "Passive"
source: "Pathfinder GM Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You comb through information to learn more about the topic at hand. Choose your research topic, section of the library, or other division depending on the form of research, and attempt a skill check. The skills to use and the DC for the check depend on the specific research task, and the Research activity gains any traits appropriate to the type of research (such as linguistic when perusing books).
- **Critical Success** You gain 2 RP.
- **Success** You gain 1 RP.
- **Critical Failure** You make a false discovery and lose 1 RP.

**Source:** `= this.source` (`= this.source-type`)
