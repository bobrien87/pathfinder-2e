---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]"]
cast: "`pf2:0`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** Your previous action was to Sustain your manifested realm

**Effect** Your manifested realm further corrupts more of your surroundings. Increase your manifested realm's radius by 10 feet.

**Source:** `= this.source` (`= this.source-type`)
