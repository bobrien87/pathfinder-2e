---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Viking|Viking]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Viking Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

From childhood, you have been exposed to traditional viking combat techniques, and you soon learned to handle axe, sword, and shield in battle. Now, you can raid proudly alongside your fellows. You gain the [[Shield Block]] reaction. Additionally, you have familiarity with the [[Battle Axe]], [[Hatchet]], [[Longsword]], [[Shield Boss]], [[Shield Spikes]], and [[Shortsword]]—for the purposes of proficiency, you treat any of these weapons as simple weapons.

At 5th level, whenever you get a critical hit with one of these weapons, you get its critical specialization effect.

**Source:** `= this.source` (`= this.source-type`)
