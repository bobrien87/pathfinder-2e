---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Archfiend|Archfiend]]"
source-type: "Remaster"
level: "16"
traits: ["[[Mythic]]"]
prerequisites: "Archfiend Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can teleport across the battlefield, disappearing and appearing in a burst of hellfire and brimstone, a flash of lightning, a cloud of caustic gas, or other environmental hazard common within your planned realm. You can cast [[Translocate]] as a 4th-rank divine innate spell at will. When you do, spaces adjacent to the one you leave from and the one you appear in are momentarily filled with a damaging energy common to your realm, dealing @Damage[4d6[@actor.flags.system.realmDamage]|options:area-damage|shortLabel] damage of your realm's damage type to creatures in the affected spaces ([[Reflex]] save against your class DC or spell DC, whichever is higher).

**Source:** `= this.source` (`= this.source-type`)
