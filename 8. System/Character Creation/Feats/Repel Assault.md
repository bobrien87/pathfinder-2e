---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Mythic]]"]
prerequisites: "Guardian's Calling"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An enemy's attack would deal damage equal to or greater than your level to you or an adjacent ally.

Your Calling demands that you defy danger and injury to yourself or those who rely on you while allowing you to respond to the originators of such aggression with ferocious and unrivaled fury. Spend a Mythic Point; you gain resistance to the triggering attack equal to your level. If you Strike the enemy that made the attack before the end of your next turn, you can make that Strike at mythic proficiency. This benefit applies only to the first Strike you make against that enemy.

**Source:** `= this.source` (`= this.source-type`)
