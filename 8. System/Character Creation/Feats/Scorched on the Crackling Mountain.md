---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Tanuki]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

By ritualistically marking your fur with fire, like an infamous tanuki of legend, you protect yourself against future flames. You gain a black stripe down your back that looks charred. Your flat check to remove persistent fire damage is DC 10 instead of DC 15, which can be reduced to DC 5 with appropriate assistance. The first time each day you would be reduced to 0 Hit Points by a fire effect, you avoid being knocked out and remain at 1 Hit Point, and your wounded condition increases by 1. Two hairs plucked from your tail can be used as flint and steel to create a fire, emitting a strange crackling sound as they ignite.

**Source:** `= this.source` (`= this.source-type`)
