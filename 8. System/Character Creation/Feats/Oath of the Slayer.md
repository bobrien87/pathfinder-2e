---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Champion]]", "[[Oath]]"]
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

During your daily preparations, you can swear an oath to defeat, topple, or destroy a certain kind of enemy during your deeds that day. Choose aberrations, celestials, dragons, fiends, or undead. You can't choose celestials if you're holy, nor can you choose fiends if you're unholy. You gain an edict to banish or slay creatures of that kind.

Your Strikes and devotion spells that deal damage do an additional 1 spirit damage against a creature with the chosen trait. This damage increases to 2 at 7th level and 3 at 14th level. If a creature with the chosen trait triggers your champion's reaction, this additional damage doubles until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
