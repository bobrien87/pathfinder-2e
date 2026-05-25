---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Artillerist|Artillerist]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Artillerist Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

By loading special ammunition in a particular way, you can make your siege weapons do all manner of tricks that other siege engineers can barely even imagine. If you personally contribute an additional Load action to the siege weapon's loading, above the minimum, you can change a burst into a line twice as long as the size of the burst, or vice versa (so a @Template[type:burst|distance:10] turns into a @Template[type:line|distance:20], or a @Template[type:line|distance:20] turns into a @Template[type:burst|distance:10]).

**Source:** `= this.source` (`= this.source-type`)
