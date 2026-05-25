---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Inventor]]", "[[Manipulate]]"]
prerequisites: "offensive boost"
frequency: "once per PT10M"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per 10 minutes

You don't just tinker with your own innovation, you fiddle with your allies' weapons as well (for their benefit, of course). Choose an ally in your reach and one of their weapons. Attempt a [[Crafting]] check against a high DC for your level.
- **Success** For 1 minute, the chosen ally's Strikes with the chosen weapon gain the same offensive boost your innovation has.

> [!danger] Effect: Helpful Tinkering
- **Critical Failure** Your ally takes damage of the type and amount that your offensive boost normally deals on a successful Strike.

**Source:** `= this.source` (`= this.source-type`)
