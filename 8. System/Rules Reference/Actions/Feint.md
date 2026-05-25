---
type: action
source-type: "Remaster"
traits: ["[[Mental]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You are within melee reach of the target you attempt to Feint.

With a misleading flourish, you leave an opponent unprepared for your real attack. Attempt a Deception check against your target's Perception DC.
- **Critical Success** You throw your enemy's defenses against you entirely off. The target is [[Off Guard]] against melee attacks that you attempt against it until the end of your next turn.
- **Success** Your foe is fooled, but only momentarily. The target is off-guard against the next melee attack that you attempt against it before the end of your current turn.
- **Critical Failure** Your feint backfires. You are off-guard against melee attacks the target attempts against you until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
