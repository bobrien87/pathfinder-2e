---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Duelist|Duelist]]"
source-type: "Remaster"
level: "12"
traits: ["[[Archetype]]"]
prerequisites: "Duelist Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Dueling is your art, and your weapon is your instrument. You have studied and evaluated a great many combat techniques, which you can review each day without fail to ensure you are prepared for any and every situation that may occur. During your daily preparations, you can swap out any number of your duelist archetype feats for other duelist archetype feats of the appropriate level for which you are qualified. You can't swap out Duelist Dedication or Student of the Dueling Arts in this way.

In addition, you can enter a stance from a duelist archetype feat you don't have (such as one listed under Additional Feats) by increasing the number of actions it takes to enter the stance by 1 (typically to 2 actions). You must still meet the stance feat's prerequisites.

**Source:** `= this.source` (`= this.source-type`)
