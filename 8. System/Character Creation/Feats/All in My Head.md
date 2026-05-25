---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Bard]]", "[[Illusion]]", "[[Mental]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You would take damage from a Strike or spell that doesn't have the death trait or otherwise cause instant death (such as [[Disintegrate]]).

Using your occult connections and incredible powers of persuasion, you convince yourself that the triggering damage is a figment of your imagination. The damage changes from its usual damage type to mental damage, and the damaging effect gains the nonlethal trait. You can't use this reaction if you are immune to mental effects or mental damage.

**Source:** `= this.source` (`= this.source-type`)
