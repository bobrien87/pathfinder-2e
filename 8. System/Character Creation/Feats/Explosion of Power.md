---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Sorcerer]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your magic explodes. You know the following blood magic effect.

**Blood Magic—Explosion of Power** Raw power explodes outward from you. Each creature within a @Template[emanation|distance:5] takes 1d6 damage per rank of the spell you just cast (basic Reflex save). The type of damage depends on the tradition of your bloodline. If you cast arcane spells, you deal force damage. If you cast divine spells, you deal spirit damage. If you cast occult spells, you deal mental damage. If you cast primal spells, you deal fire damage.

**Source:** `= this.source` (`= this.source-type`)
