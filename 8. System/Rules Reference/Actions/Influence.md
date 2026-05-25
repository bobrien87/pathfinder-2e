---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Linguistic]]"]
cast: "Passive"
source: "Pathfinder GM Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You attempt to make a favorable impression on an NPC to convince the NPC to support your cause. Attempt a skill check to impress that NPC. The DC and skills which can apply can be found in the NPC's stat block.
- **Critical Success** You gain 2 Influence Points with the chosen NPC.
- **Success** You gain 1 Influence Point with the chosen NPC.
- **Failure** You gain no Influence Points with the chosen NPC.
- **Critical Failure** You lose 1 Influence Point with the chosen NPC.

**Source:** `= this.source` (`= this.source-type`)
