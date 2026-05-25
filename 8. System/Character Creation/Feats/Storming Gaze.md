---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Hungerseed]]", "[[Primal]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can open or energize a notable third eye on your forehead to strike with storming power. You deal @Damage[(ceil(@actor.level/2))d4[@item.flags.system.rulesSelections.stormingGaze]|options:area-damage]{3d4 electricity or 3d4 sonic damage} in a @Template[type:cone|distance:15]; Storming Gaze gains this trait. Each creature in the area must attempt a [[Reflex]] save saving throw against the higher of your class DC or spell DC. You can't use this ability again for 1d4 rounds.

At 7th level and every 2 levels thereafter, the damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
