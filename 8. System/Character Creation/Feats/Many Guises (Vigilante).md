---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Vigilante|Vigilante]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "master in Deception, Vigilante Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can take on any number of mundane guises.

Whenever you change your identity, instead of taking on your social or vigilante identity, you can become someone completely ordinary. This identity isn't a specific individual—rather, you become a nondescript member of your ancestry, of any gender, and from a mundane occupation such as common laborer, farmer, or peasant.

Spells and abilities detect you as if you were this ordinary identity, rather than either of your two real identities, unless they succeed at a counteract check against the same Deception DC used for Vigilante Dedication. Using class or dedication abilities ends this disguise.

**Source:** `= this.source` (`= this.source-type`)
