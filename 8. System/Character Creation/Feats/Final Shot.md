---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Gunslinger]]"]
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirement** You're wielding an unloaded firearm.

You jam a triple charge of black powder into your weapon to unleash a devastating but risky and inaccurate attack. Interact to reload, expending three doses of black powder in addition to your normal black powder or ammunition, then Strike with your firearm against a creature within the weapon's first range increment. If you roll a success, the attack is instead a critical success, but if you roll a failure, the weapon misfires. Regardless of your roll, after the attack you're [[Off Guard]] until the start of your next turn and [[Stunned]] 1.

**Source:** `= this.source` (`= this.source-type`)
