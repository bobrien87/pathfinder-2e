---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Flourish]]", "[[Guardian]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Putting your weight behind your weapon's swing, you can push one enemy into another. Make a melee Strike against an enemy of your size or smaller. If you hit and deal damage, you can move the enemy up to 5 feet (up to 10 feet on a critical hit) in a direction of your choice. It must remain within your reach during this movement, and you can't move it into or through obstacles. You can move the target into another creature's space. If you do, the second creature takes bludgeoning damage equal to @Damage[(2*(@actor.abilities.str.mod))[bludgeoning]]{double your Strength modifier} and is pushed away from the target until it's no longer in the same space. If there's no room for the second creature to move, you can't move the target into it.

**Source:** `= this.source` (`= this.source-type`)
