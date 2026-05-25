---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Druid]]", "[[Sonic]]", "[[Spellshape]]"]
prerequisites: "storm order"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your lightning splits the air, generating a booming shock wave. If your next action is to Cast a Spell that has the electricity trait or deals electricity damage, has no duration, and requires creatures to attempt a saving throw, the force of the spell's lightning creates a thunderclap, in addition to its other effects. Each creature that failed its Reflex save against the spell is [[Deafened]] for 1 round, and those who critically failed are also knocked [[Prone]].

**Source:** `= this.source` (`= this.source-type`)
