---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Animist]]", "[[Apparition]]", "[[Wandering]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your attuned apparition ensures that even if you would be distracted or disrupted, your magic does not go to waste. If a reaction would disrupt your spellcasting action, attempt a flat check. If you succeed, your action isn't disrupted. When you gain the third apparition class feature, this DC is reduced to 13, and when you gain the fourth apparition class feature, this DC is reduced to 10.

**Source:** `= this.source` (`= this.source-type`)
