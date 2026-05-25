---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Tattooed Historian|Tattooed Historian]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "Constitution +1, trained in Belkzen Lore, Orc Lore, Orc Pantheon Lore, or (at the GM's discretion) a related Lore skill"
source: "Pathfinder #207: The Resurrection Flood"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You become trained in Diplomacy or Performance; if you are already trained in both skills, you instead become trained in a skill of your choice. You gain access to all uncommon magical tattoos with the orc trait.

You gain a [[Storied Skin]] for free upon gaining this feat (or another magical tattoo of 2nd level or lower if you already have storied skin). You cannot have more than one storied skin tattoo, but the frequency of its Living History ability increases by one use per minute for every three tattooed historian feats you have. For every two tattooed historian feats you have, you can invest one magical tattoo that does not count against the maximum number of items you can have invested at one time.

**Source:** `= this.source` (`= this.source-type`)
