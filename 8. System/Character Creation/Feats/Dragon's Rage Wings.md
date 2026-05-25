---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Barbarian]]", "[[Morph]]", "[[Rage]]"]
prerequisites: "dragon instinct"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You sprout dragon wings from your back of the same color as your chosen dragon. While you are raging, you gain a fly Speed equal to your land Speed. If you are flying when your rage ends, you start to fall, but your transformation doesn't revert until the last moment, so you take no damage from the fall and land standing up. This action gains the trait of your dragon instinct's tradition.

**Source:** `= this.source` (`= this.source-type`)
