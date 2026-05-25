---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Barbarian]]", "[[Concentrate]]", "[[Rage]]"]
prerequisites: "giant instinct"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You extend your body and prepare to attack foes outside your normal reach. Until your rage ends, all your melee weapons and unarmed attacks gain a reach of 10 feet. This doesn't increase the reach of any weapon or unarmed attack that already has the reach trait, but it does combine with abilities that increase your reach due to increased size, such as Giant's Stature.

**Source:** `= this.source` (`= this.source-type`)
