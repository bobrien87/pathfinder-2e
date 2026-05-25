---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]"]
cast: "`pf2:2`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You are sharing the same space as a swarm or are adjacent to a troop

**Effect** Spend 1 Mythic Point and attempt an Intimidation check at mythic proficiency against the Will DC of the required swarm or troop. On a failure, the target Strides in a direction of your choosing and you move along with it. On a success, the target Strides twice in a direction of your choosing and you can decide whether or not to move along with it. No matter the result, the target is [[Stunned]] 1 and temporarily immune to your Overawe Crowd for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
