---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Timewracked|Timewracked]]"
source-type: "Remaster"
level: "14"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Mythic]]", "[[Occult]]"]
prerequisites: "Timewracked Dedication"
frequency: "once per day"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Cost** the Price of the chosen item

**Frequency** once per day

You can manipulate time to produce an item in a seemingly impossible fashion. You flicker a few times as you make adjustments to your gear, then solidify again with a specific needed item that you purchased from an alternate timeline using coin you have on your person. This allows you to purchase a single common item with a level no higher than your level and its Bulk must be low enough that carrying it wouldn't have made you encumbered. You must spend the standard amount to purchase the item, and this money must be carried on your person. You can be wearing or holding the item, as long as you have the required number of hands free, and if the item has the invested trait, you have already Invested in it, provided you haven't reached your limit of invested items.

**Source:** `= this.source` (`= this.source-type`)
