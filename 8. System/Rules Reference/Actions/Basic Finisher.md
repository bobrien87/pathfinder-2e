---
type: action
source-type: "Remaster"
traits: ["[[Finisher]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You make a graceful, deadly attack. Make a Strike; if you hit and your weapon qualifies for [[Precise Strike]], you deal the full 1d6 damage from precise strike.

**Source:** `= this.source` (`= this.source-type`)
