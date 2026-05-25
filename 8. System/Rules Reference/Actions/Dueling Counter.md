---
type: action
source-type: "Remaster"
traits: ["[[Magical]]"]
cast: "`pf2:r`"
source: "Pathfinder GM Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** Your opponent Casts a Spell from the same tradition as your tradition focus.

**Requirements** You are in a duel and have a tradition focus.

Expend a prepared spell or spell slot. You then attempt to counteract the triggering spell with the expended spell.

**Source:** `= this.source` (`= this.source-type`)
