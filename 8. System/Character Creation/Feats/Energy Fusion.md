---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Concentrate]]", "[[Sorcerer]]", "[[Spellshape]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You fuse two spells together, combining their energy types. If the next action you use is to Cast a Spell that deals energy damage, select a non-cantrip spell in your spell repertoire that deals a different type of energy damage, and expend an additional spell slot of the same rank as this secondary spell.

The spell you cast deals additional damage equal to the rank of the secondary spell slot expended. The spell's total damage is divided evenly between the energy type of the spell you cast and the energy type of the secondary spell.

**Source:** `= this.source` (`= this.source-type`)
