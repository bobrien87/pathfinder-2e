---
type: action
source-type: "Remaster"
traits: ["[[Brandish]]", "[[Commander]]", "[[Incapacitation]]", "[[Tactic]]"]
cast: "`pf2:2`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You and your allies currently outnumber enemies on the battlefield, and you or a squadmate have reduced an enemy to 0 Hit Points since the start of your last turn.

At your proclamation that victory is already at hand, your allies march forward with an authoritative stomp, scattering your enemies in terror. Signal all squadmates within the aura of your banner; you and each ally can Step as a free action directly toward a hostile creature. Any hostile creatures within 10 feet of a squadmate after this movement must attempt a [[Will]] save against your class DC; on a failure they become [[Fleeing]] for 1 round, and on a critical failure they become fleeing for 1 round and [[Frightened]] 2. This is an emotion, fear, and mental effect.

**Source:** `= this.source` (`= this.source-type`)
