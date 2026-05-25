---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Bloodrager|Bloodrager]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Fortune]]"]
prerequisites: "Bloodrager Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You fail a flat check to Cast a Spell or your spell would be disrupted by another creature's reaction.

The magical potency of your blood will not be denied. You finish Casting the Spell, then become [[Drained]] 1 or increase the value of your drained condition by 1.

**Source:** `= this.source` (`= this.source-type`)
