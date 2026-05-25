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

**Frequency** once per minute

**Trigger** You're about to attempt a saving throw against a linguistic effect

**Effect** Your devil's eye crackles with infernal glee as you discover a loophole in the wording of the triggering effect. You roll your saving throw twice, taking the higher result.

**Source:** `= this.source` (`= this.source-type`)
