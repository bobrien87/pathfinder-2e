---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Druid]]"]
prerequisites: "Animal Companion"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your animal companion has grown up over the course of your adventures, becoming a mature animal companion and gaining additional capabilities.

Your animal companion has greater independence. During an encounter, even if you don't use the Command an Animal action, your animal companion can still use 1 action that round on your turn to Strike or Stride (or Burrow, Climb, Fly, or Swim if it has that Speed). It can do this at any point during your turn, as long as you aren't currently taking an action. If it does, that's all the actions it gets that round—you can't Command it later.

**Source:** `= this.source` (`= this.source-type`)
