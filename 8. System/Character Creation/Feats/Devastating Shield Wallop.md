---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Flourish]]", "[[Guardian]]"]
prerequisites: "Shield Wallop"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The impact of your shield sends foes tumbling to the ground. When you use Shield Wallop, after its other effects, the target attempts a [[Fortitude]] save saving throw against your class DC. If your shield is a tower shield, fortress shield, or another shield that grants a higher circumstance bonus to AC when you [[Take Cover]] behind it, the target takes a –2 circumstance penalty to this saving throw.
- **Critical Success** The target takes no additional effect.
- **Success** The target is [[Off Guard]] to you until the end of the current turn.
- **Failure** The target is knocked [[Prone]].
- **Critical Failure** The target is knocked prone and [[Stunned]] 1.

**Source:** `= this.source` (`= this.source-type`)
