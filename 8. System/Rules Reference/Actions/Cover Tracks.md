---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Exploration]]", "[[Move]]"]
cast: "Passive"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You cover your tracks, moving up to half your travel Speed, using the Travel Speed rules. You don't need to attempt a Survival check to cover your tracks, but anyone tracking you must succeed at a [[Survival]] check against your Survival DC if it is higher than the normal DC to [[Track]].

In some cases, you might Cover Tracks in an encounter. In this case, Cover Tracks is a single action and doesn't have the exploration trait.

**Source:** `= this.source` (`= this.source-type`)
