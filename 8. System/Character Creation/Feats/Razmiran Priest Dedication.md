---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Razmiran Priest|Razmiran Priest]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "trained in Crafting, trained in Deception"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have earned entry to the priesthood of Razmir, either at the Exalted Lodge or another temple where Razmir's holy masks are forged. You gain a [[Razmiri Mask]] and can Craft a replacement in 4 hours if yours is ever damaged or lost. There is no value in selling your *Razmiri mask*, and only you gain its benefits. The abilities of your *Razmiri mask* use the higher of your class DC or spell DC.

You can take the [[Cleric Dedication]] feat without needing to meet its prerequisites and before you take two other feats from the Razmiran priest archetype, but you must choose Razmir as your deity. All spells granted by the cleric archetype when gained in this way are occult spells instead of divine spells, and cleric feats that normally have the divine trait instead have the occult trait. Your key spellcasting attribute for these spells is Charisma, rather than Wisdom.

Razmiran Priest

**Source:** `= this.source` (`= this.source-type`)
