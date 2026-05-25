---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Flourish]]", "[[Rogue]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You leap from hiding and assail your target. You Stride up to your Speed, but you must end your movement next to an enemy you're [[Hidden]] from or [[Undetected]] by. You then Strike that enemy; you remain hidden from or undetected by that creature until after you Strike. You can use Spring from the Shadows while Burrowing, Climbing, Flying, or Swimming instead of Striding if you have the corresponding movement type.

**Source:** `= this.source` (`= this.source-type`)
