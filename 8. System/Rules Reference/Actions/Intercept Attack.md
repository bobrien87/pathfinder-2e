---
type: action
source-type: "Remaster"
traits: ["[[Guardian]]"]
cast: "`pf2:r`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** An ally within 10 feet of you takes physical damage.

You fling yourself in the way of oncoming harm to protect an ally. You can Step, but you must end your movement adjacent to the triggering ally. You take the damage instead of the triggering ally. Apply your own immunities, weaknesses, and resistances to the damage, not the ally's.

**Special** You can extend this ability to an ally within 15 feet of you if the damage comes from your taunted enemy. If this ally is farther than you can Step to reach, you can Stride instead of Stepping; you still must end the movement adjacent to your ally.

**Source:** `= this.source` (`= this.source-type`)
