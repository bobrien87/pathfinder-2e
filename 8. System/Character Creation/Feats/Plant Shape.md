---
type: feat
source-type: "Remaster"
level: "10"
traits: ["[[Druid]]"]
prerequisites: "leaf order or Untamed Form"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You can take the shape of a plant creature. If you don't have untamed form, you can cast [[Plant Form]] once per day, heightened to the same rank as your highest-rank druid spell slot.

If you do have [[Untamed Form]], add the shapes listed in [[Plant Form]] to your [[Untamed Form]] list, and whenever you're polymorphed into another shape using untamed form, you gain resistance 5 to poison.

**Source:** `= this.source` (`= this.source-type`)
