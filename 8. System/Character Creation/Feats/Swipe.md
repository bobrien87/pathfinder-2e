---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Barbarian]]", "[[Fighter]]", "[[Flourish]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You make a wide, arcing swing. Make a single melee Strike and compare the attack roll result to the ACs of up to two enemies, each of whom must be within your melee reach and adjacent to the other. Roll damage only once and apply it to each creature you hit. A Swipe counts as two attacks for your multiple attack penalty.

If you're using a weapon with the sweep trait, its modifier applies to all your Swipe attacks.

**Source:** `= this.source` (`= this.source-type`)
