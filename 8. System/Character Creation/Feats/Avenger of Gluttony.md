---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Mythic]]"]
source: "Pathfinder #220: Crypt of Runes"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've become the champion of the runelords of gluttony, and their hungry spirits are always near you. Whenever a spell or other magical effect restores Hit Points to you, you can choose to reduce the number of Hit Points you regain by any amount. The first time each day you reduce the Hit Points by an amount equal to your level, you gain 1 Mythic Point. You gain the [[Gluttonous Feast]] activity.

**Source:** `= this.source` (`= this.source-type`)
