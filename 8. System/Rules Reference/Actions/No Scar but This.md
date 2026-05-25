---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Healing]]", "[[Transcendence]]", "[[Vitality]]"]
cast: "`pf2:1`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Your wounds knit shut with hardly a scratch. You regain @Damage[(ceil(@actor.level/2))d8[healing,vitality]|shortLabel] Hit Points. At 3rd level and every 2 levels thereafter, the healing increases by 1d8.

**Source:** `= this.source` (`= this.source-type`)
