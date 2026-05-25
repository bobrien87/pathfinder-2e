---
type: action
source-type: "Remaster"
traits: ["[[Fortune]]"]
cast: "`pf2:r`"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Trigger** You critically fail a skill check with a skill you gained from the banished celestial background

**Effect** The next time you attempt a skill check using the skill that triggered this ability within the next minute, roll twice and take the higher result.

**Source:** `= this.source` (`= this.source-type`)
