---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Halcyon Speaker|Halcyon Speaker]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]"]
prerequisites: "Halcyon Spellcasting Adept"
source: "Pathfinder Claws of the Tyrant"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** You're a member of the Vellumis Scholars.

You seek to excise the rot from the Gravelands and have made progress to do so. You can cast [[Field of Life]] as a 6th-rank halcyon spell, and you gain a 6th-rank halcyon spell slot. When you cast your halcyon *field of life* as a primal spell, any living creatures in the area when you Sustain the spell gain a +2 status bonus to saving throws against curses, diseases, and poisons for 1 round.

> [!danger] Effect: Vellumis Excision

**Special** If you have the Halcyon Spellcasting Sage feat, you treat the *field of life* halcyon spell gained from this feat as a signature spell, even though halcyon spells normally can't be signature spells.

**Source:** `= this.source` (`= this.source-type`)
