---
type: action
source-type: "Remaster"
traits: ["[[Exploration]]", "[[Secret]]"]
cast: "Passive"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You canvass local markets, taverns, and gathering places in an attempt to learn about a specific individual or topic. The GM determines the DC of the Diplomacy check and the amount of time it takes (typically 2 hours, but sometimes more), along with any benefit you might be able to gain by spending coin on bribes, drinks, or gifts.
- **Success** You collect information about the individual or topic. The GM determines the specifics.
- **Critical Failure** You collect incorrect information about the individual or topic.

Sample Gather Information Tasks- **Untrained** talk of the town
- **Trained** common rumor
- **Expert** obscure rumor, poorly guarded secret
- **Master** well-guarded or esoteric information
- **Legendary** information known only to an incredibly select few, or only to extraordinary beings

**Source:** `= this.source` (`= this.source-type`)
