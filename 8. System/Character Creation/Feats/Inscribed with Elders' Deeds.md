---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Tattooed Historian|Tattooed Historian]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Tattooed Historian Dedication"
source: "Pathfinder #207: The Resurrection Flood"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your tattoos commemorate unique exploits that (according to legends) only an orc could accomplish. During your daily preparations, you can reconfigure part of your storied skin to depict a specific orc hero, granting you a 1st-level ancestry feat with the orc trait until you prepare again; this ancestry feat cannot require any physiological feature you lack, as determined by the GM. Since this feat is temporary, you can't use it as a prerequisite for permanent character options, such as for a feat. At 13th level, you can instead gain a 5th-level ancestry feat with the orc trait.

**Source:** `= this.source` (`= this.source-type`)
