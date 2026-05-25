---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Kineticist]]"]
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Elements are wild and dangerous, but you've found ways to reduce their risk. When you Channel Elements or use a stance impulse that affects your kinetic aura, you can designate a number of creatures up to your Constitution modifier (minimum 1 creature). Choose whether they are immune to the benefits of your kinetic aura or immune to its damage and drawbacks. You don't have to be able to see a creature to designate it, nor does it need to be in your kinetic aura, but you can't designate a creature that's unnoticed by you.

In addition, you gain the [[Pacifying Infusion]] action.

**Source:** `= this.source` (`= this.source-type`)
