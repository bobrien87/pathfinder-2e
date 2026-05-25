---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Fire]]", "[[Impulse]]", "[[Kineticist]]", "[[Overflow]]", "[[Primal]]", "[[Teleportation]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You fall through your own kinetic gate, leaving behind an effigy of flame and reappearing majestically near another fire. You instantly transport yourself, and any items you're wearing and holding, from your current space to a clear space within 120 feet you can observe that's adjacent to an open flame or a creature taking persistent fire damage. If this would bring another creature with you—even if you're carrying it in an extradimensional container—the action fails.

A whorl of fire surrounds you in a @Template[emanation|distance:5] either before you depart or after you arrive. Each creature in the area takes @Damage[(floor((@actor.level -14)/3)+4)d6[fire]|options:area-damage] damage with a [[Reflex]] save against your class DC.

**Level (+3)** The fire damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
