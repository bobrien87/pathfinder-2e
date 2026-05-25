---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Rivethun Involutionist|Rivethun Involutionist]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Rivethun Involutionist Dedication"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You gain the service of a young animal companion, which has been blessed by the spirits of this world. If you already have an animal companion, your current animal companion becomes blessed by the spirits instead. This animal companion follows all the usual rules for animal companions. You can Sustain to activate your companion's latent blessing, as long as your animal companion is within 60 feet of you. When you activate this blessing, all damage dealt by your animal companion's Strikes deal spirit damage, rather than the usual damage those Strikes would deal. This blessing remains active until the beginning of your next turn.

**Source:** `= this.source` (`= this.source-type`)
