---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Hellknight|Hellknight]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained by a Hellknight Order"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You're from Old Cheliax.

You've started walking the path toward becoming a true Hellknight, though you're currently considered only an armiger. You've been taught how to terrorize others into compliance, but you also continually study the structure and hierarchy of Hell. You must survive painful tests of your body and mind called reckonings that steady your willpower against all sorts of trauma.

You gain resistance to mental damage equal to 1 + your number of archetype class feats from the Hellknight archetype. You become trained in Intimidation; if you were already trained, you become an expert instead. In addition, you gain the [[Additional Lore]] general feat for Hell Lore; if you were already trained in Hell Lore, you also become trained in a Lore skill of your choice.

Hellknight

**Source:** `= this.source` (`= this.source-type`)
