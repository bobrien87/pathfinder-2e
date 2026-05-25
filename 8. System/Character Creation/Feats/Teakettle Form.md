---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Tanuki]]"]
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your shapeshifting is advanced enough to take the form of not just creatures, but objects as well. When you Change Shape, you can assume the form of a simple tool or object of 1 Bulk or less, such as a teakettle or umbrella. When transformed into an object, you can function as that object for allies to use; for instance, turning into a crowbar so you can help an ally pry open a crate. You can speak while in object form, but you can't attack, cast spells, or move except to [[Crawl]] (usually by hopping or flopping across the ground in an undignified manner).

**Source:** `= this.source` (`= this.source-type`)
