---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Monk]]"]
prerequisites: "Mountain Stance"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are in [[Mountain Stance]]

You focus on your connection to the earth and call upon the mountain to block attacks against you. You gain a +2 circumstance bonus to AC until the beginning of your next turn.

> [!danger] Effect: Mountain Stronghold

**Special** If you have this feat, the Dexterity modifier cap to your AC while you're in [[Mountain Stance]] increases from +0 to +1.

**Source:** `= this.source` (`= this.source-type`)
