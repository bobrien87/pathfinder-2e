---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Barbarian]]", "[[Flourish]]", "[[Rage]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding a ranged or thrown weapon that deals piercing damage.

Your projectiles are unhindered by flesh and bone. Make a ranged Strike with a ranged or thrown weapon that deals piercing damage against each creature in a @Template[line|distance:30] (this uses only one projectile despite the number of Strikes). These Strikes ignore all cover granted by creatures. Roll damage only once and apply it to each creature you hit. Each attack counts toward your multiple attack penalty, but don't increase your penalty until you have made all your attacks.

**Source:** `= this.source` (`= this.source-type`)
