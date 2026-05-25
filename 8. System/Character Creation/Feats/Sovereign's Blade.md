---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Light]]", "[[Mythic]]"]
prerequisites: "Prophesied Monarch Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a melee weapon.

As you raise your weapon into the air, it begins to shed a bright light that pierces darkness and calls your knights to your side. Spend a Mythic Point; you automatically counteract any magical darkness whose counteract rank is 7 or lower. Any knight who can see your raised weapon can immediately use their reaction to Stride up to twice directly toward you, and any of your knights who are adjacent to you after this movement get a +2 status bonus to their attack rolls until the start of your next turn.

**Source:** `= this.source` (`= this.source-type`)
