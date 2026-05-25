---
type: action
source-type: "Remaster"
traits: ["[[Rogue]]"]
cast: "`pf2:0`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** Your Strike hits an off-guard creature and deals damage

You apply one of the following debilitations, which lasts until the end of your next turn:

- **Debilitation** The target takes a –10-foot status penalty to its Speeds.
- **Debilitation** The target becomes [[Enfeebled]] 1.

**Source:** `= this.source` (`= this.source-type`)
