---
type: action
source-type: "Remaster"
traits: ["[[Incapacitation]]", "[[Rogue]]"]
cast: "`pf2:0`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** Your Strike hits an [[Off Guard]] creature and deals damage.

The target attempts a [[Fortitude]] save against your class DC. It then becomes temporarily immune to your Master Strike for 1 day.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Enfeebled]] 2 until the end of your next turn.
- **Failure** The target is [[Paralyzed]] for 4 rounds.
- **Critical Failure** The target is paralyzed for 4 rounds, knocked [[Unconscious]] for 2 hours, or killed (your choice).

**Source:** `= this.source` (`= this.source-type`)
