---
type: action
source-type: "Remaster"
traits: ["[[Fortune]]"]
cast: "`pf2:r`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per hour

**Trigger** You attempt a check to remove or counteract an effect with the [[Confused]], [[Controlled]], [[Fascinated]], [[Immobilized]], [[Paralyzed]], or [[Restrained]] conditions

**Effect** You roll twice and use the better result.

**Source:** `= this.source` (`= this.source-type`)
