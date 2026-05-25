---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Magical]]"]
cast: "`pf2:1`"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per round

**Effect** Your ostilli flashes red as it regurgitates a dart of magic at a target within 30 feet. This magical dart deals @Damage[((1+floor((@actor.level -2)/4))d6)[piercing]] damage ([[Reflex]] save against the higher of your class DC or spell DC). This damage increases by 1d6 at 6th level and every 4 levels thereafter.

**Source:** `= this.source` (`= this.source-type`)
