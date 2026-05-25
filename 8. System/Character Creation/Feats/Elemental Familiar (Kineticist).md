---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Kineticist]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

A small creature made of elemental matter springs forth from your kinetic gate. This elemental familiar appears to be made of one of your kinetic elements, though it might have unusual or distinguishing aspects. Like other familiars, your elemental familiar can assist you in various tasks and on adventures. You gain an elemental familiar with the trait of one of your kinetic elements. If you have more than one kinetic element, you can change the element you've selected for your familiar to a different one of your kinetic elements each time you make your daily preparations. The familiar uses your Constitution modifier to determine its Perception, Acrobatics, and Stealth modifiers.

**Source:** `= this.source` (`= this.source-type`)
