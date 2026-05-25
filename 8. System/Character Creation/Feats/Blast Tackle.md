---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Gunslinger]]"]
prerequisites: "way of the vanguard"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You're wielding a two-handed crossbow or a firearm that has the kickback or scatter trait.

You throw yourself at an enemy, bracing your weapon against it and pulling it close before releasing a destructive shot. Attempt to [[Grapple]]; if you're wielding your weapon in both hands, you Release one hand to do so. If your Grapple succeeds, you can immediately Strike the target of the Grapple with the required weapon, even if it's a two-handed weapon you're holding in one hand. This Strike deals an additional 3d6 precision damage.

As long the creature remains [[Grabbed]] or [[Restrained]], you can use just one hand to reload the weapon and Strike that creature with it.

**Source:** `= this.source` (`= this.source-type`)
