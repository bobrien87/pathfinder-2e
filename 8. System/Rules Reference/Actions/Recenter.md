---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]"]
cast: "`pf2:1`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You're in a psychic duel and are trained in the statistic matching the psychic center you are changing to.

You adopt the psychic center matching the emotion of your choice. If you were already psychically centered, you lose your old psychic center when you adopt the new one.

**Source:** `= this.source` (`= this.source-type`)
