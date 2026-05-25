---
type: action
source-type: "Remaster"
cast: "`pf2:r`"
source: "Pathfinder Myth-Speaker Player's Guide"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per game session

**Trigger** You would fail or critically fail an attack, check, or saving throw to which you apply mythic proficiency

**Effect** You regain 1 Mythic Point.

**Source:** `= this.source` (`= this.source-type`)
