---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Druid]]", "[[Manipulate]]", "[[Sorcerer]]", "[[Spellshape]]", "[[Wizard]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Druid** With a complex gesture, you call upon the primal power of your spell to overcome enemies' resistances.

**Sorcerer** You alter your spells to tear through an enemy's defenses.

**Wizard** Multiple circles of runes rotate around your hand as you overcharge your spell to tear through your enemy's defenses.

If the next action you use is to Cast a Spell, the spell ignores an amount of the target's resistance to acid, cold, electricity, fire, or sonic damage equal to your level. This applies to all damage the spell deals, including persistent damage and damage caused by an ongoing effect of the spell, such as the wall created by [[Wall of Fire]]. A creature's immunities are unaffected.

**Source:** `= this.source` (`= this.source-type`)
