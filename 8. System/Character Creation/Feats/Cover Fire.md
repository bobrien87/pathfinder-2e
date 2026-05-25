---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Gunslinger]]"]
frequency: "once per round"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per round

**Requirements** You're wielding a loaded firearm or crossbow.

You lay down suppressive fire to protect allies by forcing foes to take cover from your wild attacks. Make a firearm or crossbow Strike; the target must decide before you roll your attack whether it will duck out of the way. If the target ducks, it gains a +2 circumstance bonus to AC against your attack, or a +4 circumstance bonus to AC if it has cover. It also takes a -2 circumstance penalty to ranged attack rolls until the end of its next turn. If the target chooses not to duck, you gain a +1 circumstance bonus to your attack roll for that Strike.

**Source:** `= this.source` (`= this.source-type`)
