---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Tengu]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You gain access to all uncommon weapons with the tengu trait plus the katana, khakkara, temple sword, and wakizashi. You have familiarity with these weapons—for the purpose of proficiency, you treat any of these that are martial weapons as simple weapons and any that are advanced weapons as martial weapons.

During your daily preparations, you can practice with a weapon from the sword group that's in your possession. You gain familiarity with that weapon as well. This lasts until you practice with a different sword in the same way.

At 5th level, whenever you get a critical hit with one of these weapons, you get its critical specialization effect.

> [!danger] Effect: Sword Practice

**Source:** `= this.source` (`= this.source-type`)
