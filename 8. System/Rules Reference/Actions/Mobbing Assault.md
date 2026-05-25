---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]"]
cast: "`pf2:1`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** Your horde has been raised

**Effect** Each enemy in a @Template[type:emanation|distance:5] around your horde takes @Damage[(ternary(gte(@actor.level,18),8,ternary(gte(@actor.level,14),6,ternary(gte(@actor.level,10),4,2))))d6[bludgeoning]|options:area-damage] damage (if your horde is zombies) or @Damage[(ternary(gte(@actor.level,18),8,ternary(gte(@actor.level,14),6,ternary(gte(@actor.level,10),4,2))))d6[slashing]|options:area-damage] damage (if your horde is skeletons) with a [[Reflex]] save against your spell DC. At 10th level and every 4 levels thereafter, the damage increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
