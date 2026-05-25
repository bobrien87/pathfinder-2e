---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Yaksha]]"]
prerequisites: "Yaksha heritage with an edict that requires you to confront a certain type of creature"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You become trained in the Lore skill corresponding to one creature type mentioned by your vow (for example, Fey Lore if your heritage is deny the firstborn pursuit). Whenever you successfully Recall Knowledge about this type of creature, you gain a +1 circumstance bonus to AC and saving throws against that creature's attacks and abilities for 1 round.

> [!danger] Effect: Avowed Insight

**Source:** `= this.source` (`= this.source-type`)
