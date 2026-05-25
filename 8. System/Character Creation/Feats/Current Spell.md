---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Druid]]", "[[Spellshape]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

As you use your magic to manipulate air or water, you spin off some of its currents to form a barrier around you. If your next action is to [[Cast a Spell]] with the air or water trait, until the start of your next turn, you gain a +1 circumstance bonus to AC or a +2 circumstance bonus against ranged attacks. This effect has the air or water trait, or both, depending on the traits of the spell you cast. You also gain a +1 circumstance bonus to all saves against effects with the air trait, water trait, or both until the start of your next turn, depending on the spell's traits.

> [!danger] Effect: Current Spell

**Source:** `= this.source` (`= this.source-type`)
