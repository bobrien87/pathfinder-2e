---
type: feat
source-type: "Remaster"
level: "13"
traits: ["[[Kobold]]"]
prerequisites: "Dracomancer"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your draconic power equals that of a lesser dragon. Choose one 3rd-rank spell and one 4th-rank spell from those listed for a dragon spellcaster of your draconic benefactor's type (for example, [[Clairvoyance]] and [[Paralyze]] for a conspirator dragon benefactor). You can cast each of these spells once per day as innate spells of the same tradition as your draconic benefactor.

**Source:** `= this.source` (`= this.source-type`)
