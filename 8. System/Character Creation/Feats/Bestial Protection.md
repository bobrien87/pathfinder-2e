---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Beastmaster|Beastmaster]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Emotion]]", "[[Fear]]", "[[Mental]]"]
prerequisites: "Beastmaster Dedication, animal companion that's Large or greater"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your companion's mere presence is enough to rattle creatures that fall under its shadow. When a creature adjacent to your animal companion that's smaller than it targets you with an attack, that creature becomes [[Frightened]] 1.

**Source:** `= this.source` (`= this.source-type`)
