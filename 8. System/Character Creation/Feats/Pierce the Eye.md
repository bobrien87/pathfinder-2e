---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Eternal Legend|Eternal Legend]]"
source-type: "Remaster"
level: "16"
traits: ["[[Mythic]]"]
prerequisites: "Eternal Legend Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding a ranged weapon.

You aim a shot from your weapon directly at a foe's eye, blinding them in the process. Make a ranged Strike. On a hit, the target additionally takes 2d8 persistent bleed damage. The target must also attempt a [[Fortitude]] save against your class DC with the following effects.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Blinded]] until the end of its next turn.
- **Failure** The target is blinded for as long as they are taking the persistent bleed damage and for 1 additional round thereafter.
- **Critical Failure** As failure, but the target also takes a –2 circumstance penalty to the flat check to remove the persistent bleed damage; a creature Administering First Aid to stop this persistent bleed damage takes a –2 circumstance penalty to the Medicine check.

> [!danger] Effect: Pierce the Eye

**Source:** `= this.source` (`= this.source-type`)
