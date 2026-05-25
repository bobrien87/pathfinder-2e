---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Bard]]"]
prerequisites: "warrior muse"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your muse has taught you how to handle a wider variety of weapons than most bards, empowering you to effortlessly blend your performance into combat tools. When you have a [[Courageous Anthem]] composition cantrip active, and you damage an enemy with a Strike, the spell's duration is extended by 1 round. You can extend an individual casting only once in this way.

If you gain the [[Rallying Anthem]] or [[Song of Strength]] composition cantrips, you can apply this benefit to those cantrips as well.

**Source:** `= this.source` (`= this.source-type`)
