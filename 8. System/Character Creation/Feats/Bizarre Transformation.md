---
type: feat
source-type: "Remaster"
level: "14"
traits: ["[[Druid]]", "[[Manipulate]]", "[[Spellshape]]"]
prerequisites: "Untamed Form"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The forms you take on defy belief—chimerical sights of twisted antlers or acidic drool. If your next action is to cast [[Untamed Form]], you can change the damage type of a single unarmed attack granted by *untamed form* to one of the following: acid, bludgeoning, cold, electricity, fire, poison, piercing, or slashing. The chosen attack gains the appropriate trait.

**Source:** `= this.source` (`= this.source-type`)
