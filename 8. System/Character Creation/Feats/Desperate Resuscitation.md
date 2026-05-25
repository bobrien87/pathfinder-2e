---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Commander]]", "[[Healing]]", "[[Manipulate]]"]
prerequisites: "master in Medicine, Officer's Medical Training"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are holding a [[Healer's Toolkit]] or are wearing one and have a free hand; the target's body is mostly intact; the target was not killed by a death effect.

You can use your training in combat medicine to revive the recently deceased. Attempt a DC 40 [[Medicine]] check to revive a dead creature that has been dead for no more than 3 rounds. If you succeed, the target returns to life with the effects of [[Raise Dead]], except it still has the wounded condition it had before dying, increased by 1 (or [[Wounded]] 1 if it wasn't wounded before dying). Whether you succeed or fail, the target is temporarily immune to Desperate Resuscitation for 1 day.

**Source:** `= this.source` (`= this.source-type`)
