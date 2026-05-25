---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Air]]", "[[Electricity]]", "[[Impulse]]", "[[Kineticist]]", "[[Overflow]]", "[[Primal]]", "[[Sonic]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Dark thunderclouds swirl in a miniature storm, crisscrossed with lightning bolts; a tremendous thunderclap fills the air. The storm appears in a @Template[burst|distance:20] within 60 feet. Each creature in the area takes @Damage[(floor((@actor.level -8)/3)+3)d12[electricity],1d10[sonic]|options:area-damage] damage, with a [[Reflex]] save against your class DC. A creature that fails its save is [[Deafened]] until the end of its next turn (or for 1 minute on a critical failure). A creature wearing metal armor or made of metal takes a -1 circumstance penalty to its save.

**Level (+3)** The electricity damage increases by 1d12.

**Source:** `= this.source` (`= this.source-type`)
