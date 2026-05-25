---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Concentrate]]", "[[Divine]]", "[[Exemplar]]", "[[Light]]", "[[Spirit]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You critically hit an enemy this turn.

You let out a war cry as your blow lands true, and judgment descends on an enemy. A pillar of light deals @Damage[ternary(gte(@actor.level,17),10,ternary(gte(@actor.level,12),7,4))d6[spirit]] damage with a [[Reflex]] save against your class DC to a different enemy selected at random within 30 feet of the target struck. This damage increases to 7d6 if you are 12th level and 10d6 if you are 17th level.

**Source:** `= this.source` (`= this.source-type`)
