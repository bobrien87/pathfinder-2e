---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Kobold]]"]
prerequisites: "dragonscaled kobold heritage"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The study of dragons is not merely academic to you but part of your family tree. Tracking lineages, benefactors, and communities has become second nature. You become trained in Intimidation and your choice of Arcana, Nature, Occultism, or Religion. For each of these skills in which you were already trained, you become trained in a skill of your choice. You also gain the Additional Lore general feat for Dragon Lore.

**Source:** `= this.source` (`= this.source-type`)
