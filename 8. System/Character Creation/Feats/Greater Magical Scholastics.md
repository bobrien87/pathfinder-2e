---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Archaeologist|Archaeologist]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]"]
prerequisites: "Archaeologist Dedication, Magical Scholastics"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You broaden your magical studies, allowing you to find the right path, detect hidden objects, and conceal those objects from unscrupulous rivals.

You can cast [[Augury]], [[Locate]], and [[Veil of Privacy]] as occult innate spells, each once per day. You can cast this *veil of privacy* spell only on an object, and it's automatically heightened to half your level rounded up.

**Source:** `= this.source` (`= this.source-type`)
