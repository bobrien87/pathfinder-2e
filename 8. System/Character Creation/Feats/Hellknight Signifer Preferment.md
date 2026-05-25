---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Hellknight|Hellknight]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]"]
prerequisites: "Hellknight Dedication, passed the Hellknight Test, trained in Hellknight breastplate, you have a spellcasting class feature"
source: "Pathfinder Lost Omens Hellfire Dispatches"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've bolstered your force of will with the power of the Measure and the Chain. You've officially joined the ranks of Hellknight signifers, and you receive a [[Signifer's Mask]], often devoid of eyeholes or other decorative features. The mask doesn't obscure your vision, though it makes it impossible for others to see your eyes. While wearing your signifer's mask, you gain a +1 circumstance bonus to Deception checks to `act lie`, Intimidation checks to `act coerce`, and Deception DCs against `act sense-motive`. You gain expert proficiency rank in Intimidation (or in another skill in which you're trained of your choice, if you were already an expert in Intimidation), as well as in your choice of Arcana, Nature, Occultism, or Religion.

**Special** You can't take both this feat and [[Hellknight Errant]] or [[Hellknight Preferment]].

**Source:** `= this.source` (`= this.source-type`)
