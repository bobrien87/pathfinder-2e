---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Cleric]]"]
frequency: "once per turn"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per turn

**Trigger** You finish Casting a Spell using one of your divine spell slots on your turn.

You siphon residual spell energy into a weapon you're wielding. Until the end of your turn, the weapon deals an additional 1d4 spirit damage. If you are holy or unholy, Strikes with the weapon also gain that trait, and the additional damage increases to 2d4 against creatures of the opposing trait.

**Source:** `= this.source` (`= this.source-type`)
