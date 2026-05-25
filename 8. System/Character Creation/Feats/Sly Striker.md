---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Rogue]]"]
prerequisites: "sneak attack"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your attacks deal more damage, even against creatures that aren't [[Off Guard]]. When you succeed or critically succeed at a Strike against a creature that isn't off-guard, you also deal 1d6 precision damage. This applies only if you're using a weapon or unarmed attack you could deal sneak attack damage with.

At 14th level, if you would normally deal 3d6 or more sneak attack damage to off-guard creatures, you deal 2d6 precision damage to creatures that aren't off-guard.

**Source:** `= this.source` (`= this.source-type`)
