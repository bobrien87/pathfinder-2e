---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Monk]]", "[[Stance]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are unarmored

You enter the stance of impenetrable iron, refusing to yield to any blow. You can make iron sweep unarmed attacks. These deal 1d8 bludgeoning damage; are in the brawling group; and have the nonlethal, parry, sweep, and unarmed traits.

While in Ironblood Stance, you gain resistance 2 to all damage. The resistance increases to 3 at 12th level, to 4 at 16th level, and to 5 at 20th level.

> [!danger] Effect: Stance: Ironblood Stance

**Source:** `= this.source` (`= this.source-type`)
