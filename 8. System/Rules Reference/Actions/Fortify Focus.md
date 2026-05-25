---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]"]
cast: "`pf2:2`"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You are touching your designated companion, and their focus pool isn't full

**Effect** Your companion regains 1 Focus Point.

**Source:** `= this.source` (`= this.source-type`)
