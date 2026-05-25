---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Barbarian]]", "[[Druid]]", "[[Mental]]"]
prerequisites: "animal instinct or untamed order"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your last action dealt bludgeoning damage using an unarmed Strike granted by a morph or polymorph effect.

You've learned how to cloud your foes' minds with the brutal impact of your repeated attacks. Make an unarmed Strike against the same target. If the Strike hits and deals bludgeoning damage, the target is [[Stupefied 2]] for 1 round ([[Stupefied 3]] on a critical hit).

**Source:** `= this.source` (`= this.source-type`)
