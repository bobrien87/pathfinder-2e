---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Fighter]]"]
prerequisites: "Aggressive Block or Brutish Shove"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can push larger foes around with your attack. You can use [[Aggressive Block]] or [[Brutish Shove]] against a creature up to two sizes larger than you.

When a creature you Shove or knock back with a shield, polearm, or club's critical specialization effect has to stop moving because it would hit an object, it takes @Damage[@actor.abilities.str.mod]{damage} equal to your Strength modifier (minimum 1).

**Source:** `= this.source` (`= this.source-type`)
