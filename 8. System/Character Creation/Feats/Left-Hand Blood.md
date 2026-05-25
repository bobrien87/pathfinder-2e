---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Kholo]]"]
frequency: "once per PT1H"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per hour

It's said that the flesh of the right side of a hyena can heal diseases, but that the flesh of the left side is deadly and poisonous. You deal @Damage[1[slashing]|immutable:true] damage to yourself to poison a weapon you are holding. If you hit with the weapon and deal damage, the target also takes 1d4 persistent,poison damage. The poison on your weapon becomes inert after you hit, or at the end of your next turn, whichever comes first.

> [!danger] Effect: Left Hand Blood

**Source:** `= this.source` (`= this.source-type`)
