---
type: action
source-type: "Remaster"
traits: ["[[Brandish]]", "[[Commander]]", "[[Tactic]]"]
cast: "`pf2:2`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You call for a careful retreat. Signal all squadmates within the aura of your banner; each can immediately Step up to three times as a free action. Each Step must take them farther away from at least one hostile creature they are observing and can only take them closer to a hostile creature if doing so is the only way for them to move toward safety (such as if they're surrounded).

**Source:** `= this.source` (`= this.source-type`)
