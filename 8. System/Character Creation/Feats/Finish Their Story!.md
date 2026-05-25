---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Eternal Legend|Eternal Legend]]"
source-type: "Remaster"
level: "20"
traits: ["[[Mythic]]"]
prerequisites: "Eternal Legend Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Though your tale is immortal, your foes aren't afforded such an advantage and mainly serve only to further your legend. When the time is right, you can shepherd a weaker opponent off this mortal coil. Spend a Mythic Point and make a Strike at mythic proficiency against an enemy. This Strike counts as two attacks for your multiple attack penalty and either kills or damages the target depending on their level, as noted below. After you make this Strike, the target becomes temporarily immune to Finish Their Story!, for 1 hour.

**16th Level or Lower** If the Strike hits, the target dies instantly.

**17th Level** If the Strike hits, the target takes the Strike's normal damage plus an additional three damage die.

**18th Level or Higher** If the Strike hits, the target takes the Strike's normal damage plus an additional two damage die.

**Source:** `= this.source` (`= this.source-type`)
