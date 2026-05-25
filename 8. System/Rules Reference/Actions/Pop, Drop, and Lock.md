---
type: action
source-type: "Remaster"
traits: ["[[Brandish]]", "[[Commander]]", "[[Tactic]]"]
cast: "`pf2:2`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per 10 minutes

You command your squadmates to perform a devastating coordinated takedown. Signal up to three squadmates within the aura of your commander's banner who all have the same enemy within their reach; the squadmates can attempt to Strike, [[Trip]], or [[Grapple]] the opponent as a reaction. Each squadmate can only attempt one specific action granted by this tactic, the actions can be attempted in any order and a specific action can only be attempted once as part of this tactic.

**Source:** `= this.source` (`= this.source-type`)
