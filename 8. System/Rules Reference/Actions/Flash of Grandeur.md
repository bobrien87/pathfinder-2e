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

**Effect** Imperious divine light flashes out from you to surround your foe. The ally gains resistance to all damage against the triggering damage equal to 2 + your level. Until the end of your next turn, the attacker is affected by [[Revealing Light]].

> [!danger] Effect: Champion's Resistance

**Source:** `= this.source` (`= this.source-type`)
