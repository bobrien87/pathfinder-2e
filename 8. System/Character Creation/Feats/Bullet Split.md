---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Flourish]]", "[[Gunslinger]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a firearm or crossbow in one hand and a slashing (or versatile S) melee weapon in the other.

You carefully align your weapon with the edge of your blade, splitting the projectile in two as you fire to attack two different targets. Make two Strikes, one each against two separate targets. The targets must be adjacent to each other and within your weapon's maximum range. Each of these attacks takes a –2 penalty to the attack roll, but the two count as only one attack when calculating your multiple attack penalty.

**Source:** `= this.source` (`= this.source-type`)
