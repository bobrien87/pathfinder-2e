---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Artillerist|Artillerist]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in martial weapons"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Artillery is a team sport, where every member of the crew has to rely on the other members. At best, a mistake might just waste time. At worst, a misaligned fuse or a badly set pin could cause the whole thing to explode. You've taken these lessons to heart, and so your presence on an artillery team assists the entire team at every aspect of the siege weapon's deployment and usage. If you're serving on a siege weapon crew, you and all other members gain a +2 circumstance bonus to any checks to Load, Aim, move, or Repair the weapon. When you Aim a siege weapon, you can move the weapon's aim twice as far as normal.

Artillerist

**Source:** `= this.source` (`= this.source-type`)
