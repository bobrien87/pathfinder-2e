---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Monk]]"]
prerequisites: "Deflect Projectile, Monastic Archer Stance"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are in [[Monastic Archer Stance]], are wielding a bow, and have a free hand.

Snatching an arrow out of the air, you instantly put it to your bow and return fire. When you successfully [[Deflect Projectile]] that's an arrow, as part of that reaction you can immediately make a ranged bow Strike from your own bow by firing the arrow you deflected.

**Source:** `= this.source` (`= this.source-type`)
