---
type: action
source-type: "Remaster"
traits: ["[[Automaton]]"]
cast: "`pf2:r`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** A critical hit deals physical damage to you.

Attempt a DC 17 flat check. If you are successful, the attack becomes a normal hit.

**Source:** `= this.source` (`= this.source-type`)
