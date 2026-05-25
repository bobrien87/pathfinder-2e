---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Infusion]]", "[[Kineticist]]"]
prerequisites: "two or more kinetic elements"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Slamming one element into another, you combine their strengths. If the next action you use is an [[Elemental Blast]], choose two of your kinetic elements instead of one. The blast gains the traits of both elements and uses the highest range and damage die among the two elements. Half the blast's damage is the damage type of one element, and the other half is the damage type of the other element. If the total damage is an odd number, you choose which element deals the higher damage. Determine the damage amounts before altering the amount due to halving, doubling, resistances, weaknesses, and other calculations. If either element can deal more than one type of damage, you can still choose which damage type to use. You gain any added effects of both elements, such as their critical blast junction effects.

**Source:** `= this.source` (`= this.source-type`)
