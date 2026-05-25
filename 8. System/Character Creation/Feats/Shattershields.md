---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Metal]]", "[[Primal]]", "[[Stance]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Four plates of pitted metal float around you to intercept attacks. You and allies in your kinetic aura gain a +1 circumstance bonus to AC. When any creature with this bonus would take damage from a physical attack, one of the plates reduces the damage by its Hardness of 5. If the damage exceeds the Hardness, that plate is destroyed. You can replenish all destroyed plates as a single action that has the concentrate trait.

**Level (+2)** The Hardness increases by 1.

**Source:** `= this.source` (`= this.source-type`)
