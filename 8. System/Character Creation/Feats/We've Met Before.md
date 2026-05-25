---
type: feat
source-type: "Remaster"
level: "2"
traits: ["[[Mythic]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You've spent at least 1 minute in mutual conversation with a creature.

Your ability to discern information about those you interact with is without peer. Spend a Mythic Point to gain a Lore skill specific to the required creature for the next 24 hours; you have mythic proficiency with that skill and can use it to Recall Knowledge about the creature, Decipher Writings created by the creature, [[Earn Income]] or Subsist in areas ruled by the creature, or perform other appropriate tasks as determined by the GM.

**Source:** `= this.source` (`= this.source-type`)
