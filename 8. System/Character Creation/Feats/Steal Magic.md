---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Mythic]]"]
prerequisites: "Mythic Counterspell"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You don't just counter your enemy's magic, you instantly master it and make it your own. When you successfully counterspell an enemy's spell using Mythic Counterspell, you can learn that spell as long as it's on the spell list for your tradition. If you have a spellbook, the spell is instantly scribed into the book, creating new blank pages if needed. If you have a spell repertoire, you can instantly retrain any spell currently in your repertoire to the countered spell, though if the spell you replace is one granted to you by a class feature (such as an animist's apparition spells or a sorcerer's bloodline spells), the spell reverts to the one normally granted by that class feature during your next daily preparations.

**Source:** `= this.source` (`= this.source-type`)
