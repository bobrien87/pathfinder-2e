---
type: action
source-type: "Remaster"
traits: ["[[Manipulate]]"]
cast: "`pf2:1`"
source: "Pathfinder Adventure: Prey for Death"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You can Interact with your shroud, swirling it around you, to gain a +1 circumstance bonus to AC until the beginning of your next turn.

**Source:** `= this.source` (`= this.source-type`)
