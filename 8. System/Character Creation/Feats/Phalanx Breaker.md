---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Gunslinger]]"]
prerequisites: "Way of the Vanguard"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a two-handed firearm or a two-handed crossbow.

You know that to take out an enemy formation, you must punch a hole through its center. Make a ranged Strike with the required weapon against a target within the weapon's first range increment. The target is pushed directly back 10 feet (20 feet on a critical hit), and if this pushes the target into an obstacle, the target takes bludgeoning damage equal to half your level.

**Source:** `= this.source` (`= this.source-type`)
