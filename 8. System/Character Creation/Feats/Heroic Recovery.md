---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Spellshape]]"]
prerequisites: "healing font"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The restorative power of your healing invigorates the recipient. If the next action you use is to cast [[Heal]] targeting a single living creature and the target regains Hit Points from the spell, the target also gains three bonuses until the end of its next turn: a +5-foot status bonus to its Speed, a +1 status bonus to attack rolls, and a +1 status bonus to damage rolls. In addition, if the target is [[Prone]], it can immediately Stand as a free action that doesn't trigger reactions.

> [!danger] Effect: Heroic Recovery

**Source:** `= this.source` (`= this.source-type`)
