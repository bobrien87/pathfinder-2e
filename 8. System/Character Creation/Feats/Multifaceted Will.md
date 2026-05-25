---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Seneschal|Seneschal]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Seneschal Witch Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Without the firm hand of a patron, your power begins to reflect deeper complexities, sometimes latching onto entirely unexpected sources of magical potency. When you cast or Sustain [[Manifest Will]], you can choose any tradition's manifestation. While the spell is active, you and allies in its area gain a +1 status bonus to saves against spells with that tradition trait.

**Source:** `= this.source` (`= this.source-type`)
