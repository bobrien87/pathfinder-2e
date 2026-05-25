---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Mythic]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a shield or a weapon with the parry trait.

You're the bulwark that doesn't break. Spend a Mythic Point, and Raise a Shield or position the required weapon to parry; for the next minute, whenever you Raise a Shield or position a weapon to parry (including when you first use this ability), all allies you can see gain the shield or weapon's circumstance bonus to AC. When your shield is raised or your weapon is positioned to parry while this effect is active, enemies treat all squares within your reach as difficult terrain. When using the Shield Block reaction, after the block is complete, you can attempt a Strike with a shield bash or an attached weapon on the required shield (such as a shield boss or shield spikes) against an adjacent enemy at mythic proficiency.

The first time each round an enemy misses you with a melee Strike while your weapon is positioned to parry, you can Strike them with that weapon at mythic proficiency as a reaction.

> [!danger] Effect: Unbreaking Castle

**Source:** `= this.source` (`= this.source-type`)
