---
type: action
source-type: "Remaster"
traits: ["[[Mental]]", "[[Psyche]]", "[[Psychic]]"]
cast: "`pf2:1`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Your subconscious automatically calculates vectors and forces when your mind is unleashed, showing you the likely path of incoming attacks to avoid. You gain a +2 circumstance bonus to AC and Reflex saves until the beginning of your next turn.

**Source:** `= this.source` (`= this.source-type`)
