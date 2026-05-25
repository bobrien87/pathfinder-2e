---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Metal]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You would take acid, electricity, fire, or sonic damage.

You absorb energy and hold it in your kinetic gate. You gain resistance equal to your level to the triggering damage—choose one eligible type of resistance. If this reaction prevents any damage, you gain a status bonus equal to half your level to the damage roll of the next metal impulse you use before the end of your next turn.

> [!danger] Effect: Consume Power

**Source:** `= this.source` (`= this.source-type`)
