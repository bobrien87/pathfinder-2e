---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Archer|Archer]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Concentrate]]"]
prerequisites: "Archer Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You slow down, focus, and take a careful shot. Make a ranged Strike with a weapon in the bow or crossbow weapon group. You gain a +2 circumstance bonus to the attack roll and ignore the target's [[Concealed]] condition. If the target is [[Hidden]], reduce the flat check from being hidden from 11 to 5.

**Source:** `= this.source` (`= this.source-type`)
