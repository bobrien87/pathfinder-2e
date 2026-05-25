---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Impulse]]", "[[Kineticist]]", "[[Primal]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You turn an element into its purest form. Choose one of your kinetic elements and target up to 1 cubic foot of that element within 30 feet. (One cubic foot of liquid is roughly 8 gallons.) You remove toxins and pollutants from the element as well as anything intruding into the element, such as plant roots in soil. This can't change the grade of a material, alter the form of a manufactured object, or change the structural integrity of the element. If the purification would remove an alchemical or magical pollutant (such as a poison or curse), Purify Element attempts to counteract that impurity, using your class DC - 10 for the counteract check. If it fails to counteract a particular impurity, any further attempt you make to counteract that impurity with Purify Element fails as well.

**Source:** `= this.source` (`= this.source-type`)
