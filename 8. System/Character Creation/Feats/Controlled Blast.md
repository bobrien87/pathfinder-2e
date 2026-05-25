---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Demolitionist|Demolitionist]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Demolitionist Dedication, Bomber's field discovery, Directional Bombs, or Expanded Splash"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You maximize the effectiveness of your explosives by controlling every possible parameter of the blast meticulously. If you have the [[Directional Bombs]] feats, you can use it with [[Set Explosives]] or [[Demolition Charge]], even though you didn't throw the bombs. If you have the Bomber's Field Discovery or [[Expanded Splash]] feats, you can apply the additional splash damage to one of the bombs when you Set Explosives or use Demolition Charge, and you can apply the increased splash area from Expanded Splash to all the bombs.

**Source:** `= this.source` (`= this.source-type`)
