---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Morph]]", "[[Primal]]", "[[Water]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You adapt a creature to living and moving in water. Target a willing creature within 30 feet. For 10 minutes, it gains the effects of a [[Feet to Fins]] spell, can breathe water, and gets a +1 status bonus to AC and saves against any creature with the amphibious, aquatic, or water trait. In addition, its attacks ignore the effects water normally has on bludgeoning and slashing attacks. If you use Return to the Sea again, any existing one ends.

**Level (6th)** You can target up to 5 willing creatures.

**Source:** `= this.source` (`= this.source-type`)
