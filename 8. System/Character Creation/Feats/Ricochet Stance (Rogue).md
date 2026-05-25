---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Rogue]]", "[[Stance]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You adopt a stance to rebound your thrown weapons toward you. While you are in this stance, any thrown weapons you use as part of a ranged Strike to deal bludgeoning or slashing damage immediately return to your hand, enabling you to use them for additional Strikes. You must be within the weapon's listed range increment and have a hand free to catch the weapon. If you make a ranged Strike with a thrown weapon outside of its listed range increment, it instead flies back toward you a number of feet equal to its listed range increment and then falls to the ground.

**Source:** `= this.source` (`= this.source-type`)
