---
type: action
source-type: "Remaster"
traits: ["[[Healing]]"]
cast: "`pf2:r`"
source: "Pathfinder Spore War Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per minute

**Trigger** You arrive at a location via a teleportation effect

**Effect** When you reappear after the teleportation, your body takes advantage of the teleportation to put itself back together in a healthier state, and you restore a number of Hit Points equal to 1d6 plus your level plus your Intelligence modifier (@Damage[(1d6 + @actor.level + @actor.system.abilities.int.mod)[healing]]).

**Source:** `= this.source` (`= this.source-type`)
