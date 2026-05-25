---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have a [[Harm]] or [[Heal]] spell you can cast.

You balance both sides of the scales, restoring yourself while striking a foe. Cast a 1-action *harm* or *heal* spell to heal yourself, expending the spell normally. It loses the manipulate trait when cast this way. Then make a melee Strike. If you make this Strike with your deity's favored weapon, you gain a +1 status bonus to the attack roll.

If the Strike hits, you can target a second willing creature to heal the same amount from the spell. This creature can be outside of the spell's range, provided it's adjacent to the enemy you hit.

**Source:** `= this.source` (`= this.source-type`)
