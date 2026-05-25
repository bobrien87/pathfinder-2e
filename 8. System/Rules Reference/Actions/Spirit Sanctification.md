---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Spellshape]]"]
cast: "`pf2:1`"
source: "Pathfinder Claws of the Tyrant"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Cost** 1 spirit wisp

**Effect** You immediately purify a spirit, which grants you a protective blessing before it departs. If your next action is to cast a halcyon spell, you gain a +1 status bonus to saving throws as well as resistance to void damage equal to the rank of the halcyon spell. These effects last for 1 round.

**Source:** `= this.source` (`= this.source-type`)
