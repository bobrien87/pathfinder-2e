---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Battle Harbinger|Battle Harbinger]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Battle Harbinger Dedication"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've expanded your divine capabilities, granting you magic that better supports your combat focus. You gain two special 2nd-rank creed spell slots, which can be used to prepare [[Resist Energy]], [[See the Unseen]], [[Sure Strike]], and [[Water Breathing]] as divine spells. At 10th level, the extra slots increase to 3rd rank and you add [[Haste]] and [[Heroism]] to the spells you can prepare in your creed spell slots. At 14th level, the extra slots increase to 4th rank and you add [[Fly]] and [[Unfettered Movement]].

**Source:** `= this.source` (`= this.source-type`)
