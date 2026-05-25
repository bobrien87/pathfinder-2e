---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Wizard]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can prepare two spells in one slot, giving you the freedom to choose the spell when you cast it. When you prepare your spells for the day, you can choose one spell slot at least 1 rank lower than the highest-rank spell you can cast and prepare two spells in that slot. When you Cast a Spell from that slot, choose which spell to cast. Once you've chosen, the unused spell dissipates as though you hadn't prepared it at all—for example, it isn't available for use with [[Drain Bonded Item]].

**Source:** `= this.source` (`= this.source-type`)
