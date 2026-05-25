---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Talisman Dabbler|Talisman Dabbler]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You are trained in the use of talismans and similar magical paraphernalia. This training might have occurred in a formal classroom or been an accumulation of folk magic picked up over time. You can craft talismans and know the formulas for all common talismans of your level or lower. You remember talisman formulas and don't need a formula book for them.

Additionally, you carry a vast collection of magical baubles you can turn into temporary talismans. Each day during your daily preparations, you can make two talismans with an item level no higher than half your level. You must know each talisman's formula. A talisman created this way is a temporary item and loses its magic the next time you make your daily preparations if you haven't already used it. Any saving throw DC required by a temporary talisman you create uses the highest of your class DC, spell DC, or the talisman's DC.

Finally, when you Affix a Talisman, you can (in any combination) affix or remove up to four talismans in the 10-minute span.

Talisman Dabbler

**Source:** `= this.source` (`= this.source-type`)
