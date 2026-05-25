---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Spellshape]]", "[[Witch]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An ally within 30 feet Casts a Spell.

You rhyme with your ally's incantations or echo their movements, linking your magic to empower their spell in one of two ways:

- If their spell deals damage and doesn't have a duration, you grant that spell a status bonus to damage equal to its rank.

> [!danger] Effect: Coven Spell

- If their spell doesn't have a spellshape effect applied to it, apply the effects of any one spellshape feat you know to the spell. The spellshape feat must be one that can be applied to the triggering spell, and you must be able to use it (for instance, if the spellshape feat is usable only a limited number of times per day).

**Source:** `= this.source` (`= this.source-type`)
