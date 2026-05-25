---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Flourish]]", "[[Gunslinger]]"]
prerequisites: "Way of the Drifter"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a firearm or crossbow in one hand, and your other hand is either wielding a melee weapon or is empty.

You move in and out of range to complement your attacks. You Step, make a Strike, Step, and make another Strike. One Strike must be a ranged Strike using your firearm or crossbow, and the other must be a melee Strike using your melee weapon or unarmed attack. You can choose not to take one or both Steps.

**Source:** `= this.source` (`= this.source-type`)
