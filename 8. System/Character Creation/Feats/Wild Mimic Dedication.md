---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Wild Mimic|Wild Mimic]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Nature"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Fighting in the wilds has honed your understanding of the unique abilities many creatures have. You're trained in Wild Mimic Lore, a special Lore skill that can be used only to [[Recall Knowledge]] about creatures to learn their abilities. If you have legendary proficiency in Nature, you gain expert proficiency in Wild Mimic Lore, but you can't increase your proficiency in Wild Mimic Lore by any other means. When you succeed at a Wild Mimic Lore to Recall Knowledge, you gain a +1 circumstance bonus to your saving throws against the next attack or ability that the subject of your Recall Knowledge targets you with.

> [!danger] Effect: Wild Mimic Dedication

Wild Mimic

**Source:** `= this.source` (`= this.source-type`)
