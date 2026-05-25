---
type: action
source-type: "Remaster"
traits: ["[[Commander]]", "[[Tactic]]"]
cast: "`pf2:2`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per day

Your squad performs a brutal combination attack that levels an enemy and attempts to put them down permanently. Choose and signal up to three squadmates within the aura of your commander's banner. Each squadmate can Stride up to half their Speed directly toward a single enemy you designate as a free action. Any who end their movement adjacent to the designated target can attempt to [[Trip]] or Strike it as a reaction.

The first time a [[Prone]] enemy is successfully dealt damage by a Strike from this tactic, they must immediately attempt a [[Fortitude]] save against your class DC or die; this is a death and incapacitation effect. All enemies who witness a creature slain by Bloody Guillotine must succeed at a [[Will]] save against your class DC or become [[Sickened]] 1 for 1 round ([[Sickened]] 2 for 1 round on a critical failure); this is an emotion and mental effect.

**Source:** `= this.source` (`= this.source-type`)
