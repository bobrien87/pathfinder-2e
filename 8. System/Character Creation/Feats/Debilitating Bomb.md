---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Additive]]", "[[Alchemist]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can add a crystalline additive to an alchemical bomb to have it undermine your enemy. Choose [[Dazzled]], [[Deafened]], [[Off Guard]], or a –5-foot status penalty to Speeds. If the attack with the bomb hits, in addition to the bomb's normal effects, the target must succeed at a [[Fortitude]] save saving throw or take that effect until the start of your next turn. Use your class DC for this saving throw, even if someone else throws the bomb.

**Source:** `= this.source` (`= this.source-type`)
