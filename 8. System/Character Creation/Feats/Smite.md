---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Champion]]", "[[Concentrate]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You single out one enemy to destroy in your deity's name. Designate one enemy you can see. Until the start of your next turn, your Strikes against that enemy gain a +3 status bonus to damage, increasing to +4 if you have master proficiency with the weapon or unarmed attack you're using for the Strike. If you're holy or unholy and the target has the opposite trait, the bonus is +4 (or +6 if you're a master).

If the target takes a hostile action against you or one of your allies before the start of your next turn, the duration extends to the end of that enemy's next turn. If the enemy continues to take these hostile actions each turn, the duration continues to extend.

Your current Smite ends if you use the Smite action again.

**Source:** `= this.source` (`= this.source-type`)
