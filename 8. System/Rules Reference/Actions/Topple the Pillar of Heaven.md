---
type: action
source-type: "Remaster"
traits: ["[[Transcendence]]"]
cast: "`pf2:2`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

Your ikon extends to an impossible length, striking all in its way. You deal @Damage[(max(6,floor(@actor.level / 2)))d8[untyped]|options:area-damage] damage to all creatures in a @Template[type:line|distance:60], with a [[Reflex]] save against your class DC. The damage type matches that of your weapon. At 14th level and every two levels thereafter, the damage increases by 1d8.

**Source:** `= this.source` (`= this.source-type`)
