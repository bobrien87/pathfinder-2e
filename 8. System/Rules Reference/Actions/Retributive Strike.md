---
type: action
source-type: "Remaster"
traits: ["[[Champion]]", "[[Divine]]"]
cast: "`pf2:r`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** An enemy damages your ally, and both are in your champion's aura

**Effect** You protect your ally and strike your enemy. The ally gains resistance to all damage against the triggering damage equal to 2 + your level. If the enemy is within reach, make a melee Strike against it.

> [!danger] Effect: Champion's Resistance

**Source:** `= this.source` (`= this.source-type`)
