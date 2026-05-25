---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Guardian]]"]
prerequisites: "Intercept Attack"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You [[Intercept an Attack]] that was made with a melee weapon by a creature you're adjacent to.

When you catch a weapon in your armor, you can move your body to wrench it from your foe's grasp. After Intercepting the Attack, attempt to [[Disarm]] the weapon used for that attack. You don't need to have a hand free, and you gain an item bonus to the Athletics check equal to the value of your armor's potency rune.

**Source:** `= this.source` (`= this.source-type`)
