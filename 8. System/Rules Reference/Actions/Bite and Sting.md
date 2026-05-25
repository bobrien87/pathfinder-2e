---
type: action
source-type: "Remaster"
cast: "`pf2:1`"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** Your swarm is outside your body

**Effect** Each creature in your swarm's space takes @Damage[(floor(@actor.level/2))d4[piercing]] damage with a [[Reflex]] save against your class DC or spell DC, whichever is higher. At 4th level and every 2 levels thereafter, the damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
