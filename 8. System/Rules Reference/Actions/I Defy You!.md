---
type: action
source-type: "Remaster"
traits: ["[[Fortune]]", "[[Mental]]"]
cast: "`pf2:r`"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You fail a save against a mental effect

**Frequency** once per hour

**Effect** You reroll the triggering save and must take the second result.

**Source:** `= this.source` (`= this.source-type`)
