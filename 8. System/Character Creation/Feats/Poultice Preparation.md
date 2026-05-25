---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Herbalist|Herbalist]]"
source-type: "Remaster"
level: "4"
traits: ["[[Archetype]]"]
prerequisites: "Herbalist Dedication"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you create an herbal elixir, you can prepare it as a poultice instead. A poultice gains the oil trait (but remains alchemical, not magical) and loses the elixir and ingested traits. You can apply a poultice by [[Interacting]] with one hand.

When you apply a poultice, in addition to the item's normal effects, the recipient can attempt an immediate flat check to recover from a single source of persistent acid, bleed, or fire damage, with the DC reduction from appropriate assistance.

**Source:** `= this.source` (`= this.source-type`)
