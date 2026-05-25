---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Illusion]]", "[[Occult]]"]
cast: "`pf2:3`"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Effect** Your tattoo helps you create a temporary cover to infiltrate a protected area or escape a dangerous situation. It casts 2nd-rank [[Illusory Disguise]] and 2nd-rank [[Ventriloquism]] on you. The duration of both effects is 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
