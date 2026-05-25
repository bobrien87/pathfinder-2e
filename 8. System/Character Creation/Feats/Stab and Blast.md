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

**Requirements** You're wielding a firearm with an attached bayonet or reinforced stock, a fire lance, or a combination weapon.

You slice or smash your opponent with the melee portion of your weapon before pulling the trigger at point-blank range. Make a melee Strike with the required weapon. If the Strike is successful, you can immediately make a ranged Strike against the same target with a +2 circumstance bonus to the attack roll. This counts as two attacks toward your multiple attack penalty, but you don't apply the multiple attack penalty until after making both attacks.

**Source:** `= this.source` (`= this.source-type`)
