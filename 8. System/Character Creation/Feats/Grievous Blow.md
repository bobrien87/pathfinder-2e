---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Martial Artist|Martial Artist]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Martial Artist Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You know how to deliver focused, powerful blows that bypass your enemies' resistances. Make an unarmed melee Strike. If this Strike hits, it deals two additional weapon damage dice and ignores an amount of resistance to physical damage (or to a specific physical damage type) equal to your level. This Strike counts as two attacks when calculating your multiple attack penalty.

If you are at least 18th level, increase the additional damage to three weapon damage dice.

**Source:** `= this.source` (`= this.source-type`)
