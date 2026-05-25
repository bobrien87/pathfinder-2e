---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Ritualist|Ritualist]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]"]
prerequisites: "Ritualist Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Elegant and expensive components are no replacement for your skill and practice at ritual casting. If a ritual has a Cost entry that has a value in gp, reduce the amount you need to spend by 10%. If you critically succeed at the primary check for a ritual, the gp value of components the ritual consumes is reduced by the same amount. For example, using resurrect to bring back a 14th-level creature normally costs 1,050 gp, but would cost you only 945 gp; and if you critically succeeded at the primary Religion check, you would spend only 840 gp.

**Source:** `= this.source` (`= this.source-type`)
