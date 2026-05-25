---
type: action
source-type: "Remaster"
cast: "`pf2:1`"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per round

**Effect** Your dragon companion Flies. If it doesn't normally have a fly Speed, it gains a fly Speed of 25 feet for this movement. If it isn't on solid ground at the end of this movement, it falls.

**Source:** `= this.source` (`= this.source-type`)
