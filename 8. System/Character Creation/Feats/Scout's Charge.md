---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Scout|Scout]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Scout Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You meander around unpredictably, and then ambush your opponents without warning.

Choose one enemy. Stride, [[Feint]] against that opponent, and then make a Strike against it. For your Feint, you can attempt a Stealth check instead of the Deception check that's usually required, using the terrain around you to surprise your foe.

**Source:** `= this.source` (`= this.source-type`)
