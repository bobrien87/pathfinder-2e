---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Sorcerer]]", "[[Witch]]", "[[Wizard]]"]
prerequisites: "Counterspell"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you successfully use [[Counterspell]] to counteract a spell that affects targeted creatures or an area, you can turn that spell's effect back on its caster. When reflected, the spell affects only the original caster, even if it's an area spell or it would normally affect more than one creature. The original caster can attempt a save and use other defenses against the reflected spell as normal.

**Source:** `= this.source` (`= this.source-type`)
