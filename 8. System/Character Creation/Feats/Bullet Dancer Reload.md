---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Bullet Dancer|Bullet Dancer]]"
source-type: "Remaster"
level: "10"
traits: ["[[Archetype]]", "[[Flourish]]"]
prerequisites: "Bullet Dancer Burn"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're in [[Bullet Dancer Stance]].

You've learned to reload your firearms with uncanny grace, the ammunition simply falling into place as though part of a well-practiced kata. You Strike with a simple firearm, and then Interact to reload that same firearm. You don't need a free hand to reload your weapon in this way.

**Source:** `= this.source` (`= this.source-type`)
