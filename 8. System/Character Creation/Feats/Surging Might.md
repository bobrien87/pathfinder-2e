---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Manipulate]]", "[[Oracle]]", "[[Spellshape]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You focus the power of your spell to overcome enemies' resistances. If the next action you use is to Cast a Spell, the spell ignores an amount of the target's resistance equal to your level against the following types of damage: spirit, vitality, and void.

This applies to all damage the spell deals, including persistent damage and damage caused by an ongoing effect of the spell. This doesn't cause the spell to ignore immunities, only resistances.

**Source:** `= this.source` (`= this.source-type`)
