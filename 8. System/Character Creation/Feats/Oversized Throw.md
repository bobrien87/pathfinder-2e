---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Barbarian]]", "[[Rage]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have one or more hands free.

With a great heave, you seize a piece of your surroundings, such as a boulder, log, table, wagon, or chunk of earth, and hurl it at your foes. The object must be your size or one size smaller than you, and it must not have too much Bulk for you to lift it in the first place. Make a ranged Strike with the object; regardless of the result, the object takes the same amount of damage it would deal on a success.

The object is a simple ranged weapon that deals 1d10 bludgeoning damage, has a range increment of 20 feet, and has the thrown weapon trait. The damage increases to 2d10 bludgeoning damage if you have [[Weapon Specialization]] in simple weapons, or 3d10 bludgeoning if you have Greater Weapon Specialization.

**Source:** `= this.source` (`= this.source-type`)
