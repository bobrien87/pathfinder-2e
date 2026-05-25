---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Razmiran Priest|Razmiran Priest]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]"]
prerequisites: "Razmiran Priest Dedication, master in Crafting"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have ascended to the 15th Step and stand among the greatest of Razmir's priests. You can Craft your *Razmiri mask* out of gold or upgrade your existing mask to a gold one in the same time it takes to Craft one made of iron. A gold *Razmiri mask* grants a +3 item bonus to Deception checks to [[Lie]] or [[Feint]], is a 14th-level item, and gains the following activation in addition to those possessed by the standard and silver masks.

**Activate—Call Upon Razmir's Wrath** `pf2:2` (concentrate, manipulate, occult)

**Frequency** once per day

**Effect** You cry out to Razmir to reveal his fiery wrath, as he did upon the unbelievers at Melcat. You cast [[Sunburst]] as an 8th-rank occult spell, but for undead targets the spell has the incapacitation trait.

**Source:** `= this.source` (`= this.source-type`)
