---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Flourish]]", "[[Guardian]]"]
prerequisites: "Hampering Stance"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are in [[Hampering Stance]].

You attack an enemy to ensure they can't move beyond your reach. Strike an enemy within your reach. If you hit and deal damage, that enemy can't use move actions to move beyond the reach of the weapon or unarmed attack you used for the Strike. The enemy can still move to other squares within reach of that weapon or unarmed attack. This effect lasts until the beginning of your next turn, until you move, or until you use that weapon or unarmed attack to make another attack, whichever comes first.

**Source:** `= this.source` (`= this.source-type`)
