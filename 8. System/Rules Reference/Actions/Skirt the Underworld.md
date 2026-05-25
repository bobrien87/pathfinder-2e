---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Illusion]]", "[[Incapacitation]]", "[[Transcendence]]"]
cast: "`pf2:2`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You skirt into the world of the dead, becoming [[Invisible]] for 1 round, then Fly up to your Speed. Each enemy adjacent to you at any point during this movement must succeed at a [[Fortitude]] save against your class DC or become [[Blinded]] for 1 minute (or permanently on a critical failure).

For each creature blinded by this effect, the duration of the granted invisibility extends by 1 round. Undead and other creatures with strong ties to the world of the dead, such as psychopomps, are immune to this effect.

**Source:** `= this.source` (`= this.source-type`)
