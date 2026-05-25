---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Monk]]"]
prerequisites: "Inner Upheaval"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can color your qi in bright elemental energy. When you cast [[Inner Upheaval]], in addition to the damage types normally available, you can deliver the extra damage with elemental magic, adding the element's trait and changing the damage type to the listed one: **air** electricity (sparking gust), **earth** bludgeoning (chunk of stone), **fire** fire (flickering flame), **metal** slashing (flying metal shards), **water** cold (wave of frigid water), or **wood** bludgeoning (pummeling pine cones).

**Source:** `= this.source` (`= this.source-type`)
