---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Divine]]", "[[Oracle]]"]
frequency: "once per day"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Trigger** Your turn begins.

**Requirements** You are [[Unconscious]] and have the [[Dying]] condition.

The crossroads between life and death is a place that can reveal many secrets. You gain the effects of an [[Augury]] spell in a strange, near-death vision. Empowered by the realization, you then lose the dying condition (becoming [[Wounded]] 1 or increasing your wounded value by 1, as normal), regain @Damage[2*@actor.level[healing]] Hit Points, and can Stand.

**Source:** `= this.source` (`= this.source-type`)
