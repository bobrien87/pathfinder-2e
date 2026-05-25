---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Mythic]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An enemy you're observing targets you with a ranged weapon Strike.

You redirect an incoming weapon or projectile and send your enemy's own attack roaring back at them, increasing its accuracy with a surge of mythic power. Spend a Mythic Point; you gain a +4 status bonus to AC against the triggering Strike. If the Strike fails, you immediately snatch the weapon or ammunition used for the attack out of the air and launch it back at the enemy, using mythic proficiency for your Strike. If the attack was made with a thrown weapon, add the weapon's runes and other effects to the attack as normal. If the triggering attack was made with a piece of ammunition that you're wielding an appropriate weapon for, you can apply your weapon's runes and other effects to the attack.

**Source:** `= this.source` (`= this.source-type`)
