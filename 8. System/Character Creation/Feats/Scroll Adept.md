---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Wizard]]"]
prerequisites: "expert in Crafting"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

During your daily preparations, you can create two temporary scrolls containing arcane spells from your spellbook. Each scroll must be of a different spell rank, and both spell ranks must be 2 or more ranks lower than your highest-rank spell. Any scrolls you create this way become non-magical the next time you make your daily preparations. A temporary scroll has no value if sold. As normal for a scroll, these are consumable items of light Bulk, and someone holding the item in one hand can Cast the Spell from it if it's on their spell list, using their spell attack modifier and spell DC.

If you have master proficiency in spell DC, you can create three temporary scrolls during your daily preparations, and if you have legendary proficiency, you can create four temporary scrolls.

**Source:** `= this.source` (`= this.source-type`)
