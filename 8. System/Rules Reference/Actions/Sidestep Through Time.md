---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Occult]]", "[[Teleportation]]"]
cast: "`pf2:r`"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You are about to attempt a Reflex saving throw against an area effect

**Effect** You slip through time to avoid a dangerous outcome. Teleport up to 10 feet in any direction. If this would take you outside of the area's effect, you don't need to attempt the Reflex save against it. You are then [[Off Guard]] for 1 round.

**Source:** `= this.source` (`= this.source-type`)
