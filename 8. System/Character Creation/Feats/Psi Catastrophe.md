---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Concentrate]]", "[[Mindshift]]", "[[Occult]]", "[[Psyche]]", "[[Psychic]]"]
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You stop holding your power back, unleashing it all in a catastrophic blast. All creatures in a @Template[emanation|distance:20] take @Damage[(@actor.level)d6[bludgeoning]|options:area-damage]{1d6 bludgeoning damage per level} with a [[Reflex]] save. Your psyche subsides as your power is expended.

**Source:** `= this.source` (`= this.source-type`)
