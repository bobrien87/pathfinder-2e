---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Ratfolk]]"]
prerequisites: "Ratspeak"
frequency: "once per day"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You give a shrill whistle and point, and a massive swarm of rats pours forth from the surrounding terrain to fill a @Template[burst|distance:30] within 120 feet. The rats scurry over the ground and climb up walls and surfaces, biting and clawing as they deal @Damage[6d8[piercing]|options:area-damage] damage to all enemies in the area. The rats continue to swarm in the area for the next minute, dealing @Damage[3d8[piercing]|options:area-damage] damage to any enemy that ends its turn in the area and transforming the area into difficult terrain (though the rats allow you and your allies to pass normally). You can Dismiss the effect.

**Source:** `= this.source` (`= this.source-type`)
