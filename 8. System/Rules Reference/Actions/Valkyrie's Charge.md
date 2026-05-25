---
type: action
source-type: "Remaster"
traits: ["[[Brandish]]", "[[Commander]]", "[[Tactic]]"]
cast: "`pf2:3`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

You and your allies defy death and defeat to make a glorious final charge. You restore @Damage[80[healing]|traits:healing] Hit Points to each squadmate within the aura of your commander's banner; this effect has the healing trait. If an affected ally was [[Unconscious]] due to their Hit Points being reduced to 0, they can immediately Stand and pick up any dropped weapons as a free action. Then, each affected squadmate can, as a free action, Stride up to twice their Speed directly toward an enemy they are observing; if they end this movement with an enemy within their reach, they can attempt to Strike that enemy as a reaction.

Squadmates can use Valkyrie's Charge while Burrowing, Climbing, Flying, or Swimming instead of Striding if they have the corresponding movement type.

**Source:** `= this.source` (`= this.source-type`)
