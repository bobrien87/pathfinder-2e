---
type: action
source-type: "Remaster"
cast: "`pf2:r`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** A creature adjacent to you hits you with a melee unarmed Strike

**Requirements** You have prepared your clothing to poison attackers

**Effect** The triggering creature is exposed to the suffused poison, and the poison becomes inert.

**Source:** `= this.source` (`= this.source-type`)
