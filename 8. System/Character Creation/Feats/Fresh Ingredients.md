---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Herbalist|Herbalist]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Herbalist Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

It is amazing the difference fresh herbs can make. When using [[Natural Medicine]] to [[Treat Wounds]], you gain the +2 circumstance bonus from having fresh ingredients, even if not in wilderness. If you do this in the wilderness, you gain a +4 circumstance bonus instead.

**Source:** `= this.source` (`= this.source-type`)
