---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Dual Weapon Warrior|Dual Weapon Warrior]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Dual-Weapon Warrior Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your last action was a [[Double Slice]], and both attacks hit the target.

When you hit with both attacks with Double Slice, you flense the target, making it bleed and creating a weak spot. The target takes 1d8 persistent bleed damage per weapon damage die of whichever of the weapons you used that has the most weapon damage dice (maximum 4d8 for a *major striking weapon*).

In addition, until the start of your next turn the target is [[Off Guard]], and its resistances to any physical damage types are reduced by 5.

> [!danger] Effect: Flensing Slice

**Source:** `= this.source` (`= this.source-type`)
