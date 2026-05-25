---
type: action
source-type: "Remaster"
cast: "`pf2:1`"
source: "Pathfinder GM Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You are in a duel and are trained in the skill for the tradition you're changing your focus to (Arcana for arcane, Occultism for occult, Nature for primal, or Religion for divine).

You change your tradition focus to another magical tradition.

**Source:** `= this.source` (`= this.source-type`)
