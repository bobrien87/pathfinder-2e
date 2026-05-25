---
type: action
source-type: "Remaster"
traits: ["[[Primal]]", "[[Water]]"]
cast: "`pf2:1`"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You raise a magical barrier of twisting currents. Until the start of your next turn, the first time you take acid or fire damage, you gain resistance to that damage equal to half your level (minimum 1). The resistance is equal to your level instead if you're submerged in water, if you already Cast a Spell with the water trait, or if you used another ability with the water trait this turn.

**Source:** `= this.source` (`= this.source-type`)
