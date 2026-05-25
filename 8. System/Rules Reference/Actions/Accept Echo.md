---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Occult]]"]
cast: "`pf2:1`"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

**Effect** You allow the echo to inhabit your body, gaining a glowing aura around you, shining pale-green irises, a resonating voice, and the silhouette of the spirit around your own body, all of which can be seen clearly by others. While in this state, you become trained in the weapon you chose and an expert in the skill you chose. Additionally, while you're in this state, the echo can speak and interact with the Universe using your body, and you gain a +4 status bonus to all saves against possession effects, as the possessing spirit protects you from other possessions.

This state lasts for 10 minutes, after which the echo disappears completely until the next time you make your daily preparations. You can Dismiss this effect.

At 7th level you become a master of the skill you chose, at 13th level you become an expert with the weapon you chose, and at 15th level you become legendary with the skill you chose.

**Source:** `= this.source` (`= this.source-type`)
