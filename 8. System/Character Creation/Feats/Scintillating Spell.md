---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Concentrate]]", "[[Light]]", "[[Sorcerer]]", "[[Spellshape]]", "[[Wizard]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your spells become a radiant display of light and color. If your next action is to Cast a Spell that doesn't have the darkness trait, has no duration, and requires creatures to attempt a Reflex save, the spell explodes in a spray of scintillating lights, in addition to its other effects. Each creature that failed its Reflex save against the spell is [[Dazzled]] for 1 round, and those who critically failed are instead [[Blinded]] for 1 round.

**Source:** `= this.source` (`= this.source-type`)
