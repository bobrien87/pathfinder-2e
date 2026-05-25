---
type: action
source-type: "Remaster"
cast: "`pf2:r`"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per 10 minutes

**Trigger** A melee Strike hits you and deals bludgeoning damage

**Effect** You gain resistance equal to your level to bludgeoning damage from the triggering Strike, then Stride up to half your Speed. You can Fly instead of Striding if you have a fly Speed.

**Source:** `= this.source` (`= this.source-type`)
