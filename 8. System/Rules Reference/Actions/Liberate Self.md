---
type: action
source-type: "Remaster"
traits: ["[[Divine]]", "[[Fortune]]"]
cast: "`pf2:1`"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Requirements** You're [[Grabbed]], [[Immobilized]], or [[Restrained]]

**Effect** Attempt to Escape, rolling the check twice and taking the better result.

**Source:** `= this.source` (`= this.source-type`)
