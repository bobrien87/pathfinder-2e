---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Alchemist]]", "[[Exploration]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are holding or wearing an alchemist's toolkit.

Sometimes, you need to adapt your alchemical mixtures to new situations. In a process that takes 10 minutes, you change an item you created with advanced alchemy into a similar item. You can change an alchemical bomb into another type of alchemical bomb, an elixir into another type of elixir, or a poison into another type of poison. If it's unclear whether two alchemical consumables are similar, the GM decides. You must know the formula for the new item, and the new item must be of the same or lower item level than the original item. The new item still keeps the infused trait, and it remains potent as long as the original item would have.

**Source:** `= this.source` (`= this.source-type`)
