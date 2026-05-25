---
type: action
source-type: "Remaster"
cast: "`pf2:r`"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** A creature takes persistent bleed damage from your bone flense spell

**Effect** You will the bone spurs to erupt in a particularly devastating manner, dealing 6d6 piercing damage (basic Fortitude save) to the triggering creature instead of the persistent bleed damage from bone flense. The duration of bone flense immediately ends.

**Source:** `= this.source` (`= this.source-type`)
