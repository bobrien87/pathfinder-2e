---
type: action
source-type: "Remaster"
traits: ["[[Downtime]]"]
cast: "Passive"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You can spend an entire day and night resting during downtime to recover Hit Points equal to your Constitution modifier (minimum 1) multiplied by twice your level.

**Source:** `= this.source` (`= this.source-type`)
