---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Guardian]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wearing medium or heavy armor.

You hit a foe with your armor to throw them off balance. Make a fist Strike even if you don't have a hand free; if you're wielding a [[Gauntlet]] or [[Spiked Gauntlet]], you can make a Strike with one of those weapons instead. The Strike gains the following additional results.
- **Critical Success** The target is [[Off Guard]] against melee attacks you attempt against it until the end of your next turn.
- **Success** The target is off-guard against the next melee attack you attempt against it before the end of your current turn.
- **Critical Failure** You are off-guard against melee attacks the target attempts against you until the end of your next turn.

**Source:** `= this.source` (`= this.source-type`)
