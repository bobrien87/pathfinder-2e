---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Guardian]]"]
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wearing medium or heavy armor and are standing adjacent to a [[Prone]] enemy.

You crush an enemy under the enormous weight of your armor. You drop prone and make a fist Strike against the prone enemy. You don't take the penalty from being prone to this Strike's attack roll, nor do you need to have a free hand to make it. If you're wielding a [[Gauntlet]] or [[Spiked Gauntlet]], you can Strike with one of those weapons instead of your fist. If you hit, you [[immobilize]] the target, and you can add your armor's item bonus to your Athletics for the [[Escape]] DC. The immobilization ends automatically if you Stand or otherwise move from the spot where you dropped prone.

**Source:** `= this.source` (`= this.source-type`)
