---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Goblin]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You know that the greatest treasures often look like refuse. You gain a +1 circumstance bonus to checks to Subsist, and you can use Society or Survival when you [[Subsist]] in a settlement.

When you Subsist in a city, you also gather valuable junk that silly longshanks threw away. You can [[Earn Income]] using Society or Survival at the same time while you Subsist, without spending any additional days of downtime. You also gain a +1 circumstance bonus to this check.

**Special** If you have the irongut goblin heritage, increase the bonuses to +2.

**Source:** `= this.source` (`= this.source-type`)
