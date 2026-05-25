---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Broken Chain|Broken Chain]]"
source-type: "Remaster"
level: "16"
traits: ["[[Auditory]]", "[[Mythic]]", "[[Sonic]]"]
prerequisites: "Broken Chain Dedication"
frequency: "once per PT1H"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

You let loose a yell of unbridled passion, which fuels your allies, and pounds against your foes. Allies within 60 feet who can hear you gain a +2 status bonus to attack rolls, Perception checks, saving throws, and skill checks for 1 minute.

> [!danger] Effect: Cry of Rebellion

Additionally, foes within 30 feet of you take @Damage[(@actor.level)d4[sonic]|options:area-damage] damage ([[Fortitude]] save against your class DC or spell DC, whichever is higher). This sonic damage increases by 1d4 at 17th level and every level thereafter.

**Source:** `= this.source` (`= this.source-type`)
