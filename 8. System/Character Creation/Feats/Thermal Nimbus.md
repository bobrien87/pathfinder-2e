---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Fire]]", "[[Impulse]]", "[[Kineticist]]", "[[Primal]]", "[[Stance]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You direct waves of warmth into or out of your kinetic gate to drastically shift the temperature around you. Choose cold or fire. You and allies in your kinetic aura gain resistance equal to your level to damage of that type. Any creature that starts its turn in your kinetic aura or moves into your aura during its turn takes @Damage[(floor(@actor.level/2))[@actor.flags.system.kineticist.thermalNimbus]] damage. Elemental resistance from a gate junction is cumulative with resistance from Thermal Nimbus.

**Source:** `= this.source` (`= this.source-type`)
