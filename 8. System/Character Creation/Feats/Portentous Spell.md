---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Manipulate]]", "[[Mental]]", "[[Oracle]]", "[[Spellshape]]", "[[Visual]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your spellcasting is rife with strange lights, mild fumes, and other captivating effects that befuddle your foes. If the next action you use is to Cast a Spell, any creature that attempts to use a reaction triggered by your Cast a Spell activity takes a –2 circumstance penalty to attack rolls and skill checks rolled as part of the reaction.

In addition, if the spell includes a spell attack or requires a saving throw, creatures you hit or that fail their saves are [[Fascinated]] with you until the start of your next turn.

> [!danger] Effect: Portentous Spell

**Source:** `= this.source` (`= this.source-type`)
