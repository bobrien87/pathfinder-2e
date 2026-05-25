---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Fortune]]", "[[Gunslinger]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** An ally misses with a ranged attack that uses a thrown weapon or ammunition. The ally must be willing to accept your assistance, you must see the attack's target, and the attack's target must be within the first range increment of your firearm or crossbow.

**Requirements** You're wielding a loaded firearm or crossbow.

Seeing your ally's attack about to go astray, you fire your weapon to right its course. Discharge your firearm and roll a d20. Your ally uses this roll instead of their own, and the attack ignores any bonuses the target would gain against the attack from lesser or standard cover, as well as the flat check if the target is [[Concealed]].

**Source:** `= this.source` (`= this.source-type`)
