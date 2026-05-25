---
type: action
source-type: "Remaster"
traits: ["[[Transcendence]]"]
cast: "`pf2:1`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** Your previous action was a successful Strike with the [[Mortal Harvest]]

**Effect** Time seems to lag as you blur across the battlefield, deciding the fate of many in a moment. Stride up to half your Speed and make another melee Strike with the mortal harvest against a different creature.

This Strike uses the same multiple attack penalty as your previous Strike, but counts toward your multiple attack penalty as normal.

**Source:** `= this.source` (`= this.source-type`)
