---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Thaumaturge]]"]
prerequisites: "Exploit Vulnerability"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can find the one weak point in a creature's scales, wards, roll further. or armor to get past its resistances. When you succeed at [[Exploit Vulnerability]], you learn about the highest of the creature's resistances that can be bypassed (for example, if the creature has resistance to physical damage except silver), if the creature has one. If you prefer, you can choose the following benefit instead of one of the usual two benefits from Exploit Vulnerability.

**Breached Defenses** You can choose this benefit only if you succeeded at Exploit Vulnerability and learned the creature has at least one resistance that can be bypassed. Choose one such resistance. Your unarmed and weapon Strikes bypass the chosen resistance.

**Source:** `= this.source` (`= this.source-type`)
