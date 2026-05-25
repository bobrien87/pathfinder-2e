---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Familiar Sage|Familiar Sage]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]", "[[Spellshape]]"]
prerequisites: "Familiar Sage Dedication"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your familiar alters the material of a spell into that of a precious metal. If the next action you use is to Cast a Spell that deals bludgeoning, piercing, or slashing damage, that damage is your choice of cold iron, silver, or steel for the purposes of weaknesses, resistances, vulnerabilities, and the like. At 14th level, adamantine is added to the list of metal choices. The spell gains the metal trait.

**Source:** `= this.source` (`= this.source-type`)
