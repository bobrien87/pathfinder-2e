---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Sorcerer]]", "[[Spellshape]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You fragment a ranged spell. If your next action is to Cast a Spell without a duration that requires an attack roll against a single target, you can choose a second target within range. You roll a single attack roll and compare the result to the AC of both targets.

This counts as one attack for your multiple attack penalty. To the second target, the spell deals half the amount of damage it would normally deal and has no effects beyond the spell's initial damage (such as imposing conditions or penalties).

**Source:** `= this.source` (`= this.source-type`)
