---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]"]
cast: "`pf2:r`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Trigger** You would take mental damage or be affected by a mental effect

**Effect** You gain a +2 circumstance bonus to Will saves and resistance to mental damage equal to your level against the triggering effect. This applies only to the initial effect, not successive saves, persistent mental damage, or other repeated effects.

**Source:** `= this.source` (`= this.source-type`)
