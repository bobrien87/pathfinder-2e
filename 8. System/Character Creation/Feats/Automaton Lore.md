---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Automaton]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have come to better understand the process that made your body and the magic that powers it. You gain the trained proficiency rank in Arcana and Crafting. If you would automatically become trained in one of those skills (from your background or class, for example), you instead become trained in a skill of your choice. You also gain the [[Additional Lore]] feat for Automaton Lore.

**Enhancement** Your gain greater understanding. Increase your proficiency rank in your choice of either Arcana or Crafting to expert. If you were already an expert in the chosen skill, increase your rank to master instead.

**Source:** `= this.source` (`= this.source-type`)
