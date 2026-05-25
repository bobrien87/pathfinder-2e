---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Barbarian]]", "[[Manipulate]]", "[[Rage]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are adjacent to an ally and have one or more hands free.

You toss your friends around the battlefield. Pick up an adjacent ally of your size or smaller and throw them to an unoccupied space you can see within 30 feet. Their movement doesn't trigger reactions. Your ally ends this movement on their feet and doesn't take damage from the fall. If your ally ends this movement within melee reach of at least one enemy, they can use their reaction to make a melee Strike against such an enemy.

**Source:** `= this.source` (`= this.source-type`)
