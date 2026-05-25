---
type: feat
source-type: "Remaster"
level: "17"
traits: ["[[Ardande]]", "[[Concentrate]]", "[[Plant]]", "[[Primal]]", "[[Wood]]"]
frequency: "once per PT1H"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** A creature targets you with an attack.

**Frequency** once per hour

With a sweep of your hand, vines and roots burst from the ground along the edge of your space between you and the attacker, creating a natural lattice of wood that grants standard cover. The circumstance bonus from the cover applies to your AC when you're determining the outcome of the triggering attack. If the triggering attack still hits and deals physical damage to you, the ward reduces the damage by 30 and is immediately destroyed. If the attack misses, the ward instead persists for 3 rounds before withering back into the earth. Creatures can cross the ward, but it's difficult terrain.

**Source:** `= this.source` (`= this.source-type`)
