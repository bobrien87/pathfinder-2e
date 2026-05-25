---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Gunslinger]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An enemy misses you with a ranged attack using a type of ammunition appropriate to your weapon (a bullet if you're wielding a firearm).

**Requirements** You're wielding an unloaded firearm or crossbow.

With a single fluid gesture, you catch a projectile out of the air, load it in your weapon, and shoot it back at the attacker. Interact to load the projectile into your weapon, then make a Strike with the required weapon against the triggering opponent. Since you're using the foe's ammunition, this Strike applies any special effects that ammunition would have (for instance, if it was [[Explosive Ammunition]], it would explode in a burst of fire if your Strike hits).

**Source:** `= this.source` (`= this.source-type`)
