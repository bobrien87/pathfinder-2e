---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Guardian]]"]
prerequisites: "trained in Athletics"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you push a foe away, you put the entire force of your armored form into it. When you successfully [[Shove]] a creature, that creature takes an amount of @Damage[(@actor.abilities.str.mod + @actor.skills.athletics.rank*(@actor.skills.athletics.rank - 1))[bludgeoning]]{bludgeoning damage equal to your Strength modifier} (or @Damage[(2*(@actor.abilities.str.mod + @actor.skills.athletics.rank*(@actor.skills.athletics.rank - 1)))[bludgeoning]]{double that amount} on a critical success). This damage increases by 2 when you become an expert in Athletics, 6 when you become a master, and 12 when you become legendary.

**Source:** `= this.source` (`= this.source-type`)
