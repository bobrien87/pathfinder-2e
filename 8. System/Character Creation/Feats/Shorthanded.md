---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Artillerist|Artillerist]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Artillerist Dedication"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Typically, a siege weapon is meant to be run by a crew with a very specific minimum number of members designed to ensure that your crew can account for every possible variable and necessity in loading, aiming, and firing the weapon. In a pinch, however, you can operate it with fewer people, provided you know what you're doing. You can operate a siege weapon with fewer than the minimum number of crew, at an increasing penalty. You and your crew take a –2 penalty to checks to Load, Aim, Launch, move, or Repair the weapon for each person below the minimum crew. The maximum number of missing minimum crew members you can handle with this feat is 5. For example, if a siege weapon had a minimum crew size of 8, you would still need a crew of 3, and you would take a –10 penalty when doing so.

**Source:** `= this.source` (`= this.source-type`)
