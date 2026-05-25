---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Fighter]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are wielding a melee weapon that can deal piercing damage.

You drive your piercing weapon into an imperceptible foe, revealing its location to your allies. Make a Strike with a piercing melee weapon. If the target is [[Concealed]], you don't need to attempt a flat check to target it, and if it's [[Hidden]], the DC of the flat check to target it is 5. If you hit and deal damage, you can drive the weapon you attacked with into the target (if it's corporeal), revealing its current position. You Release the weapon, and it becomes lodged in the target. If the target is concealed, no flat check is needed to target it, and if it's hidden, the DC of the flat check to target it is 5, and the creature can't become undetected. These benefits apply only for observers who can see your weapon stuck in the target. If the target is [[Invisible]], the weapon remains visible while lodged in it.

This benefit lasts until the weapon is removed from the creature. An adjacent creature or the target can remove the weapon with two Interact actions.

**Source:** `= this.source` (`= this.source-type`)
