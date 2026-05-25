---
type: action
source-type: "Remaster"
traits: ["[[Misfortune]]"]
cast: "`pf2:r`"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** A creature attempts a flat check to target you due to you being [[Concealed]] from it

**Effect** You flash your bright scales in the creature's eyes, making it hard for them to pinpoint your exact location. The creature must roll the flat check twice and take the worse result.

**Source:** `= this.source` (`= this.source-type`)
