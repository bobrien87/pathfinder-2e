---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Ranger]]", "[[Rogue]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You are about to roll a Perception, Stealth, or Survival check for initiative.

You visually or audibly warn your allies of danger, granting them each a +1 circumstance bonus to their initiative rolls, or a +2 circumstance bonus if you're using the [[Scout]] exploration activity. Depending on whether you use gestures or call out, this action gains either the visual or the auditory trait, respectively.

> [!danger] Effect: Scout's Warning

**Source:** `= this.source` (`= this.source-type`)
