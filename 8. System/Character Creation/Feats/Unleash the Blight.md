---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Deviant]]", "[[Magical]]", "[[Void]]"]
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You unleash the rot infecting you, spreading the blight to those nearby. All living creatures in a @Template[emanation|distance:60] take @Damage[(floor(@actor.level/2)d6)[void]|options:area-damage]{1d6 void} damage for every 2 levels you have, with a [[Fortitude]] save.

**Awakening** The blight is infectious. Creatures damaged by your blight take an additional 1d6 persistent,void damage, as they begin to decompose.

**Awakening** The blight is debilitating. Creatures damaged become [[Drained]] 1 for one round on a success, drained 1 for 1 minute on a failure, and [[Drained]] 2 for 1 minute on a critical failure.

**Source:** `= this.source` (`= this.source-type`)
