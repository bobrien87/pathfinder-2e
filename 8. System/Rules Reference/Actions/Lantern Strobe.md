---
type: action
source-type: "Remaster"
traits: ["[[Light]]", "[[Magical]]", "[[Visual]]"]
cast: "`pf2:2`"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Frequency** once per hour

**Effect** As you pulse your lantern, your emitters flash erratically, disorienting your opponents that see it. Each opponent in a @Template[cone|distance:15] must attempt a [[Fortitude]] save against your class DC or spell DC (whichever is higher). On a failure, the creature is [[Dazzled]] for 1 round. On a critical failure, the creature is [[Blinded]] for 1 round and dazzled for the following round.

**Source:** `= this.source` (`= this.source-type`)
