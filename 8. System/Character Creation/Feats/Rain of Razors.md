---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Metal]]", "[[Overflow]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Razor-sharp slivers of metal fall from the sky. Each creature in a @Template[burst|distance:20] within 60 feet takes @Damage[(floor((@actor.level -12)/2)+9)d6[slashing]|options:area-damage] damage with a [[Reflex]] save against your class DC. The razors embed in all surfaces in the area, making them hazardous terrain for 1 minute. A creature that moves through this hazardous terrain takes @Damage[(floor((max(12,@actor.level)-12)/2)+3)[slashing]] damage for every square of the area it moves into.

**Level (+2)** The initial damage increases by 1d6 and the hazardous terrain damage increases by 1.

**Source:** `= this.source` (`= this.source-type`)
