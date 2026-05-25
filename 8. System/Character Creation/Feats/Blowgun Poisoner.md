---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Alchemist]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can capably deliver toxins with a [[Blowgun]]. Your blowgun [[Strike|Strikes]] can apply injury poisons even if they deal no damage due to a creature's resistance. If you critically succeed at a blowgun Strike using a poisoned dart, the target's initial save against the poison is one degree of success worse than the creature rolls; this is a misfortune effect.

In addition, if you make a blowgun Strike while [[Hidden]] or [[Undetected]], you don't automatically become [[Observed]]. Instead, immediately attempt a [[Stealth]] check against the Perception DC of the target. If you succeed, you don't become observed, and are hidden (if you were undetected, you still become hidden rather than remaining undetected).

**Source:** `= this.source` (`= this.source-type`)
