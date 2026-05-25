---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Kobold]]"]
prerequisites: "dragonscaled kobold heritage"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The power infused into you by your draconic benefactor's presence allows you to manifest their most iconic spells. Choose one 1st-rank spell and one 2nd-rank spell from those listed for a dragon spellcaster of your draconic benefactor's type, (for example, [[Fear]] and [[Invisibility]] for a conspirator dragon benefactor). You can cast each of these spells once per day as innate spells of the same tradition as your draconic benefactor. You gain the trained proficiency rank in the spell attack modifier and spell DC statistics, and your key spellcasting attribute is Charisma.

**Source:** `= this.source` (`= this.source-type`)
