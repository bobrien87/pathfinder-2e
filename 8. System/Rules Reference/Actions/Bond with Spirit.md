---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Exploration]]"]
cast: "Passive"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You can forge a spiritual bond with a creature that is at least friendly toward you or with a terrain that you're currently in. Forming this bond takes 10 minutes, during which time you must remain adjacent to the creature or within that terrain. If the creature is intelligent, this also requires that creature's consent, and that intelligent creature can choose to sever this bond with you at any time as a free action, which has the concentrate trait. This bond lasts as long as you are within a mile of the creature or terrain, until you use Bond with Spirit again, or until you make your daily preparations.

You must be Bonded with a Spirit to cast the [[Entreat Spirit]] focus spell.

**Source:** `= this.source` (`= this.source-type`)
