---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Mythic]]"]
prerequisites: "guardian's Calling"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The hero-god of phalanxes and winds, grand Konebrys, led a force of dozens against an army of thousands. They gathered their soldiers in tight ranks, then marched against the wind to take the enemy by surprise. When a gust pushed the foes back, they struck their victorious blow.

You emulate Konebrys's tactics in pushing small forces against mighty foes. Whenever you are adjacent to an ally, creatures that attempt to [[Tumble Through]] your space take a –2 circumstance penalty to their Acrobatics check.

When you critically succeed on a melee Strike against an enemy, you can immediately attempt to [[Shove]] your target as a free action. You can spend a Mythic Point on this Shove attempt to do so at mythic proficiency.

**Source:** `= this.source` (`= this.source-type`)
