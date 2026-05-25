---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Broken Chain|Broken Chain]]"
source-type: "Remaster"
level: "16"
traits: ["[[Auditory]]", "[[Linguistic]]", "[[Mental]]", "[[Mythic]]"]
prerequisites: "Broken Chain Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You peer into the eyes of a target of your Ultimatum of Liberation, as you say aloud the names of their victims, searing them into the oppressor's mind, cursing them to feel their victims' pain. The target takes 12d6 mental damage ([[Will]] save against your class DC or spell DC, whichever is higher). If the target fails or critically fails this check, they also take 2d6 persistent,mental damage.

For the next hour, when the target stops taking this persistent damage, you or one of your allies can mention a victim's name as a single action to the target, forcing them to succeed at another [[Will]] save or begin taking the persistent damage again. This is a curse effect. Once you use Remember Their Names on a target, the target is immune to it for 24 hours.

**Source:** `= this.source` (`= this.source-type`)
