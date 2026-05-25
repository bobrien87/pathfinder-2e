---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]"]
cast: "`pf2:r`"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** You attempt a saving throw against a spell or magic effect but haven't rolled yet

**Effect** You find some kind of fault with the magic, using that flaw to protect yourself from the effect. You gain a +1 circumstance bonus to your saving throw against the triggering effect, which increases to a +2 circumstance bonus if the effect is divine and originates from a worshipper of the deity you chose for your grudge.

**Source:** `= this.source` (`= this.source-type`)
