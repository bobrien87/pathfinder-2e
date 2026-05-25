---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Hellknight|Hellknight]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Hellknight Dedication, passed the Hellknight Test, trained in Hellknight plate"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've forged your body to be able to stand toe-to-toe with a devil, and your mind has been shaped by the strictures of the Measure and the Chain. You've become a true Hellknight. You gain expert proficiency rank in Intimidation (or in another skill in which you're trained of your choice, if you were already an expert in Intimidation). You gain the armor specialization effects of Hellknight breastplate, Hellknight half plate, and Hellknight plate, and your resistance from that armor specialization is 1 higher than normal. In addition, you gain a +1 circumstance bonus to Intimidation checks while wearing any Hellknight armor.

**Special** You can't take both this feat and [[Hellknight Errant]] or [[Hellknight Signifer Preferment]].

**Source:** `= this.source` (`= this.source-type`)
