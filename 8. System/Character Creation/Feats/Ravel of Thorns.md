---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Plant]]", "[[Primal]]", "[[Stance]]", "[[Wood]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Thorny vines grow in geometric patterns on surfaces in your kinetic aura. A creature that starts its turn in the thorns takes a –10-foot circumstance penalty to its Speeds until it leaves the area. The thorns are hazardous terrain. A creature takes @Damage[(floor((@actor.level -4)/4)+2)[piercing]] damage each time it moves into one of these squares. If any square the thorns grow on is water or soil, double the hazardous terrain damage for all thorns. If you move, the thorns disappear; new thorns grow at the end of your turn.

**Level (+4)** The damage increases by 1.

**Source:** `= this.source` (`= this.source-type`)
