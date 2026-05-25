---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Flourish]]", "[[Guardian]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding a shield.

Attacks with your shield knock the sense out of your foes. Make a shield bash, [[Shield Boss]], or [[Shield Spikes]] Strike. If you hit and deal damage, the target is [[Stupefied 1]] until the start of your next turn ([[Stupefied 2]] on a critical hit). If your shield is a [[Tower Shield]], [[Fortress Shield]], or another shield that grants a higher circumstance bonus to AC when you [[Take Cover]] behind it, the creature is instead stupefied 2 if you hit and deal damage to it ([[Stupefied 3]] on a critical hit).

**Source:** `= this.source` (`= this.source-type`)
