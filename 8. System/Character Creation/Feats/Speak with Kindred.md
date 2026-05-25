---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Leshy]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have a connection with creatures that share your physiology. You can ask questions of, receive answers from, and use the Diplomacy skill with plants and fungi. You gain a +2 circumstance bonus to Diplomacy checks with plants or fungi of your kind. Generally, fungus leshies get this bonus with mushrooms and fungi; gourd leshies with gourds, melons, and similar fruiting plants; leaf leshies with deciduous trees; and vine leshies with vines and climbing plants.

**Source:** `= this.source` (`= this.source-type`)
