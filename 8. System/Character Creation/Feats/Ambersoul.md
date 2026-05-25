---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Ardande]]", "[[Lineage]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your elemental heritage is reflected in the oils and fragrances of plants, in tree resin that fossilizes into amber, or in the gentle smell of a flower. Sticky, golden sap runs through your veins instead of blood. Each time a creature deals slashing or piercing damage to you with a melee Strike, your sap coats its weapon or unarmed attack. The creature takes a –1 circumstance penalty on attack rolls with that weapon or unarmed attack until the end of its turn.

**Source:** `= this.source` (`= this.source-type`)
