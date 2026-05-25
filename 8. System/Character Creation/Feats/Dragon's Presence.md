---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Kobold]]"]
prerequisites: "dragonscaled kobold heritage"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

As kin to dragonkind, you project unflappable confidence (that collapses catastrophically against the deadliest foes). When you roll a success on a saving throw against a fear effect, you get a critical success instead. When you roll a failure against a fear effect, you get a critical failure instead.

In addition, when you attempt to [[Demoralize]] a foe of your level or lower, you gain a +1 circumstance bonus to the Intimidation check.

**Source:** `= this.source` (`= this.source-type`)
