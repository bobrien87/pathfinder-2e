---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Alter Ego|Alter Ego]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]", "[[Skill]]"]
prerequisites: "Alter Ego Dedication"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You know that for the best disguise to work, one requires not only the right skills but also the right look—luckily you can copy both using special magical techniques. When you [[Impersonate]], you don't need a disguise kit; instead, simple illusions or temporary transformations ripple over your body like mirror shards, providing the supplies that the kit ordinarily would. When you Impersonate in this way, your Impersonate activity gains the occult trait.

**Source:** `= this.source` (`= this.source-type`)
