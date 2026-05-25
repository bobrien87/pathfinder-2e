---
type: action
source-type: "Remaster"
traits: ["[[Auditory]]", "[[Linguistic]]"]
cast: "`pf2:r`"
source: "Pathfinder #204: Stage Fright"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** An ally within 30 feet would become [[Grabbed]], [[Immobilized]], [[Off Guard]], [[Prone]], or [[Restrained]]

**Effect** You call out a quick reminder to your ally about a special move you'd suggested to them at some point in the past, allowing the ally to avoid the triggering effect completely.

**Source:** `= this.source` (`= this.source-type`)
