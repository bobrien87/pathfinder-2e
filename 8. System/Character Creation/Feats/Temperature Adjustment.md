---
type: feat
source-type: "Remaster"
level: "7"
prerequisites: "master in Crafting, Herbalism Lore, or Medicine"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Access** Hwanggot origin

You learn Hwan temperature classifications for the elements—wood and water are cold elements, while fire, earth, and metal are hot elements. When you [[Prepare Elemental Medicine]], you can alter the environmental effects on the recipient's body. If you created hot elemental medicine, the recipient ignores the effects of severe cold while the medicine lasts. If you created cold elemental medicine, the recipient ignores the effects of severe heat while the medicine lasts.

**Source:** `= this.source` (`= this.source-type`)
