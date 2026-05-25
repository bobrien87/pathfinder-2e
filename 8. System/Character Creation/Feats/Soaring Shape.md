---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Druid]]"]
prerequisites: "Untamed Form"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Wings free you from the shackles of the ground below. Add the bat and bird shapes in [[Aerial Form]] to your [[Untamed Form]] list. If you have [[Insect Shape]], you also add the wasp shape to your *untamed form* list. If you have [[Ferocious Shape]], you also add the pterosaur shape to your *untamed form* list. Whenever you use *untamed form* to take a shape that grants you a specific Acrobatics modifier, you gain a +1 status bonus to Acrobatics checks.

**Source:** `= this.source` (`= this.source-type`)
