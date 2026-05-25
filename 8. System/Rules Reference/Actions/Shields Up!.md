---
type: action
source-type: "Remaster"
traits: ["[[Commander]]", "[[Tactic]]"]
cast: "`pf2:1`"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You signal your allies to ready their defenses. Signal all squadmates within the aura of your commander's banner; each can immediately Raise a Shield as a reaction. Squadmates who are wielding a parry weapon can instead position that weapon defensively as a reaction.

**Special** If one of your squadmates knows or has prepared the [[Shield]] cantrip, they can cast it as a reaction instead of taking the actions normally granted by this tactic.

**Source:** `= this.source` (`= this.source-type`)
