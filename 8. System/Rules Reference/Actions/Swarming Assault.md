---
type: action
source-type: "Remaster"
traits: ["[[Eidolon]]"]
cast: "`pf2:2`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** Your eidolon is dispersed.

Your eidolon swarms over each creature occupying its space, biting, pecking, clawing, or making similar attacks with its component bodies. It deals @Damage[(ceil(@actor.level / 2))d6|options:area-damage] damage to each creature in the area, with a [[Reflex]] save against your spell DC. You choose each time your eidolon uses Swarming Assault whether it deals piercing or slashing damage. Your eidolon then can't use Swarming Assault again for the next 1d4 rounds.

At 3rd level and every 2 levels thereafter, the damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
