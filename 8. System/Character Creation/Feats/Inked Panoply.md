---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Tattooed Historian|Tattooed Historian]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Tattooed Historian Dedication"
source: "Pathfinder #207: The Resurrection Flood"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature targets you with an attack, and you can see the attacker.

Your tattoos can briefly animate and extend from your skin, granting you a spectral shield-bearer who protects you from harm. Doing so expends one use of your [[Storied Skin]], granting you a +1 circumstance bonus to AC against the triggering attack. In addition, you gain resistance to mental, spirit, and void damage equal to twice your number of tattooed historian feats against the triggering attack.

**Source:** `= this.source` (`= this.source-type`)
