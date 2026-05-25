---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Arcane]]", "[[Extradimensional]]", "[[Magus]]"]
prerequisites: "unfurling brocade hybrid study"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your magic extends to your garments. During your daily preparations, you can weave magic into a single suit of fine or high-fashioned fine clothing with long sleeves or a train, such as a robe or cloak. This clothing becomes a set of [[Sleeves of Storage]], allowing you to store items in either the sleeves or the train (you choose which during your daily preparations). This treatment also makes the clothing more durable; its Hardness increases by an amount equal to your level, and its Hit Points increase by an amount equal to twice your level.

These benefits end if you prepare a new set of clothing, if someone else attempts to wear the clothing, or if you lose ownership of the clothing. When it ends, all items stored within the clothes fall into the nearest available space.

At 9th level, the clothing becomes [[Sleeves of Storage (Greater)]] instead.

**Source:** `= this.source` (`= this.source-type`)
