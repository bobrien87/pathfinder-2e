---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Gladiator|Gladiator]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Gladiator Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You're skilled with flashy weapons and can use them to great effect. You have familiarity with the [[Bo Staff]], [[Dueling Cape]], [[Spiked Chain]], [[Sword Cane]], [[Trident]], [[War Flail]], and [[Whip]]. For the purposes of proficiency, you treat these as simple weapons. The GM may add other martial weapons to this list as appropriate for the world or region you are playing in.

Whenever you get a critical hit with one of these weapons, you get its critical specialization effect.

**Source:** `= this.source` (`= this.source-type`)
