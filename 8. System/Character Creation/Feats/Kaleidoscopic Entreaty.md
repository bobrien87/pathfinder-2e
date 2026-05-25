---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Rivethun Emissary|Rivethun Emissary]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Spellshape]]", "[[Visual]]"]
prerequisites: "Rivethun Emissary Dedication"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

If your next action is to cast [[Entreat Spirit]], you can cause that spirit to unleash a brilliant display of color, light, and sound in a @Template[type:emanation|distance:10] centered on you. Each creature in the area must attempt a [[Fortitude]] save against your class DC or spell DC with the following results.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Dazzled]] for 1 round.
- **Failure** The creature is dazzled for 1 minute.
- **Critical Failure** The creature is [[Blinded]] for 1 round and dazzled for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
