---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Extradimensional]]", "[[Reflection]]"]
prerequisites: "Mirror-Risen"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've formed a connection with a small hand mirror, allowing you to use it as an extradimensional storage space. You can store one item of light Bulk in your mirror at a time. Storing or retrieving an item requires an Interact action and any creature can do so. While an item is stored within the mirror, the mirror reflects the item's image. You gain a +2 circumstance bonus to Stealth checks to [[Conceal the Object]] unless someone checks the mirror's reflection.

**Source:** `= this.source` (`= this.source-type`)
