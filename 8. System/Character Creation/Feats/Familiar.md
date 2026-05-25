---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Magus]]", "[[Sorcerer]]", "[[Thaumaturge]]", "[[Wizard]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Magus, Sorcerer** An animal serves you and assists your spellcasting.

**Wizard** You make a pact with a creature that serves you and assists your spellcasting.

**Thaumaturge** Whether by following occult rituals, piecing together scraps of arcane theory, or some other method, you've called forth a creature that now serves as your constant companion in your studies of the supernatural.

You gain a familiar.

**Source:** `= this.source` (`= this.source-type`)
