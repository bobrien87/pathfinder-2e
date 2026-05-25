---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Commander]]"]
prerequisites: "Battle-Tested Companion"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Accompanying you across countless battlefields has allowed your companion to unleash its full potential. The companion you gained with [[Commander's Companion]] is now a nimble or savage animal companion.

Your animal companion is more readily responsive to your will. During an encounter, even if you don't use the [[Command an Animal]] action, your animal companion can still use 1 action that round on your turn to Stride or Strike. If it does, it also gains a reaction it can use to respond to your tactics, but that's all the actions it gets that round—you can't Command it later.

**Source:** `= this.source` (`= this.source-type`)
