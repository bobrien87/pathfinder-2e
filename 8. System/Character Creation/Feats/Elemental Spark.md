---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Sprite]]"]
prerequisites: "Sprite's Spark"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** Tian Xia origin (but see **Special**)

You've learned to alter the magic of your sprite's spark, imparting them with elemental energies. The range of the unarmed strike from your sprite's spark increases to 30 feet. Choose one of the elements below. Your sprite's spark gains the versatile trait, allowing you to choose a different damage type when attacking with it. When dealing this different damage type, your sprite's spark gains the element's trait.

- **Water** versatile B

- **Wood** versatile vitality

- **Fire** versatile fire

- **Earth** versatile P

- **Metal** versatile S

**Special** If you're a kineticist, an elemental sorcerer, or a geniekin versatile heritage other than suli, you also have access to Elemental Spark, though you must take the corresponding element; for instance, a hydrokineticist would have access to water, or an ardande geniekin would have access to wood.

**Source:** `= this.source` (`= this.source-type`)
