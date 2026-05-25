---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Beast Lord|Beast Lord]]"
source-type: "Remaster"
level: "18"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Mythic]]"]
prerequisites: "Beast Lord Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You and your united companion call upon the service of others of its kind, creating figment duplicates of your companion to form a massive swarm of formidable power. Spend a Mythic Point. Your united companion becomes Gargantuan for 1 minute. It gains immunity to precision damage, resistance to physical damage equal to half your level, and a weakness to area damage equal to half your level. While in this form, your united companion gains the [[Amassed Assault]] action, which you immediately Command them to use as the final step of this activation.

**Source:** `= this.source` (`= this.source-type`)
