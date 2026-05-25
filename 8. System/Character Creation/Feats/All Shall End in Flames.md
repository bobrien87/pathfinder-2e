---
type: feat
source-type: "Remaster"
level: "18"
traits: ["[[Death]]", "[[Fire]]", "[[Impulse]]", "[[Kineticist]]", "[[Overflow]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

White-hot fire consumes everything in a cataclysmic sphere of death. The fire fills your choice of a @Template[burst|distance:30] within 500 feet or a @Template[emanation|distance:30]. This deals @Damage[13d6[fire]|options:area-damage] damage with a [[Reflex]] save against your class DC. Any creature dropped to 0 HP by this fire dies, reduced to a pile of ash.

If you die to this impulse, you return to life at the start of your next turn in the same space. When you return, you have Hit Points equal to double your level.

**Level (20th)** The damage is 15d6 fire.

**Source:** `= this.source` (`= this.source-type`)
