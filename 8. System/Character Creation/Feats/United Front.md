---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Broken Chain|Broken Chain]]"
source-type: "Remaster"
level: "14"
traits: ["[[Mythic]]"]
prerequisites: "Broken Chain Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Thanks to your powerful speeches, your movement finds allies in all sectors of society and even across enemy lines, all eager to help you accomplish your goals. If you spend a Mythic Point when you use [[Ultimatum of Liberation]], you can ask four questions related to that creature, as if you succeeded at four Recall Knowledge checks. This information comes to you over the course of the next 1 to 2 hours, representing tidbits of information you glean from local supporters. After receiving this information, the first time you roll Initiative in an encounter with the target of your Ultimatum of Liberation or their allies, you and all your allies can make your Initiative check with mythic proficiency.

**Source:** `= this.source` (`= this.source-type`)
