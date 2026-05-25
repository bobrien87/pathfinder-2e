---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Inventor]]", "[[Modification]]"]
prerequisites: "expert overdrive, weapon innovation"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your innovation has replaceable interlocking pieces that you can use to transform it into another type of weapon. When you select this feat, choose a level 0 weapon. It must be either a common weapon or another to which you have access. This weapon becomes your innovation's second configuration.

Select a new set of weapon modifications for this new configuration. You can spend two Interact actions to switch your weapon innovation between the two configurations. These actions don't need to be taken consecutively, but if you've provided the first and not the second, the weapon is non-functional as it is stranded between states. Your weapon's Bulk is always the greater Bulk of the two configurations, regardless of which configuration it's in—if one weapon is smaller than the other, you still need to keep any weapon parts on hand. Any runes on your weapon innovation affect the second weapon configuration as long as it would normally qualify for them.

**Source:** `= this.source` (`= this.source-type`)
