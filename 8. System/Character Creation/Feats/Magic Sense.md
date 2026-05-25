---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Detection]]", "[[Oracle]]", "[[Sorcerer]]", "[[Wizard]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have a literal sixth sense for ambient magic in your vicinity. You can sense the presence of magic auras as though you were always using a 1st-rank [[Detect Magic]] spell. This detects magic in your field of vision only. When you [[Seek]], you gain the benefits of a 3rd-rank *detect magic* spell on things you see (in addition to the normal benefits of Seeking). You can turn this sense off and on with a free action at the start or the end of your turn.

**Special** This feat has the trait corresponding to the tradition of spells you cast (arcane, divine, primal, or occult).

**Source:** `= this.source` (`= this.source-type`)
