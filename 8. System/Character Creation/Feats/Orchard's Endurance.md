---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Plant]]", "[[Primal]]", "[[Stance]]", "[[Wood]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Patches of bark appear on the skin of you and your nearby allies. You and your allies in your kinetic aura gain resistance 5 to bludgeoning and piercing damage. In addition, you and your affected allies roll flat checks to recover from persistent damage twice and take the higher result; this is a fortune effect.

> [!danger] Effect: Stance: Orchard's Endurance

**Level (+4)** The resistance increases by 2.

**Source:** `= this.source` (`= this.source-type`)
