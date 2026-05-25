---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Dual Weapon Warrior|Dual Weapon Warrior]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Dual-Weapon Warrior Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You know how to throw two weapons as easily as strike with them. Whenever a feat you gained from the dual-weapon warrior archetype allows you to make a melee Strike, you can instead make a ranged Strike with a thrown weapon or a one-handed ranged weapon you are wielding (weapons that need "1+" hand, such as longbows, don't qualify).

Any effects from these feats that apply to one-handed melee weapons or melee Strikes also apply to one-handed ranged weapons and ranged Strikes.

**Source:** `= this.source` (`= this.source-type`)
