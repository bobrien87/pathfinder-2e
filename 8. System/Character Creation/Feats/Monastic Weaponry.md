---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Monk]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have trained with the weaponry of your monastery or school. You gain access to uncommon weapons with the monk trait and become trained in simple and martial monk weapons. When your proficiency for unarmed attacks increases to expert or master, your proficiency rank for these weapons increases to expert or master as well. If you have familiarity with an agile or finesse weapon (such as from the Catfolk Weapon Familiarity feat), that weapon also gains the monk trait for you. You can use melee monk weapons with any of your monk feats or monk abilities that normally require unarmed attacks, though not if the feat or ability requires you to use a single specific type of attack, such as Crane Stance. If you gain the critical specialization benefit for unarmed attacks—with the expert strikes class feature, for example—you also gain it with monk weapons.

**Source:** `= this.source` (`= this.source-type`)
