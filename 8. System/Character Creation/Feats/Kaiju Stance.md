---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Monk]]", "[[Polymorph]]", "[[Stance]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You've encountered a kaiju and survived.

**Requirements** You're unarmored.

Your encounter with one of the rare forces of nature known as kaiju has imbued you with knowledge of a martial art that allows you to emulate a fraction of their power. When you enter Kaiju Stance, you become Large and are [[Clumsy]] 1. The only Strikes you can make are shattering earth attacks. These strikes deal 1d8 bludgeoning damage, are in the brawling group, and have the backswing, fatal d12, reach, and unarmed traits. On a critical success with a shattering earth attack, all creatures other than you that are within 10 feet of the target, including the target itself, take 1 point of bludgeoning splash damage per weapon damage die.

While in Kaiju Stance, you ignore difficult terrain.

**Source:** `= this.source` (`= this.source-type`)
