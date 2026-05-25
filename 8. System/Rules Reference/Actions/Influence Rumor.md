---
type: action
source-type: "Remaster"
traits: ["[[Downtime]]"]
cast: "Passive"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You spend at least 1 day of downtime attempting to manipulate the course, tone, or content of a rumor to your benefit. You need to succeed at a [[Diplomacy]] check to shift the rumor as you intend. The difficulty is determined by the GM based on the size of the community, the relative perceptiveness of the inhabitants, and the agency of other rumormongers, but it typically is no lower than DC 15 for a small village, DC 20 for a town, DC 30 for a city, or DC 40 for a metropolis.

**Source:** `= this.source` (`= this.source-type`)
