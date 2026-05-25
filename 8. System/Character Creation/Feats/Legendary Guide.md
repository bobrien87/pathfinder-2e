---
type: feat
source-type: "Remaster"
level: "15"
traits: ["[[General]]", "[[Skill]]"]
prerequisites: "legendary in Survival"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You know the wilderness so well that you can help your party travel through it with ease.

When you are setting the path for your party through wilderness terrain, your party gains a +10-foot circumstance bonus to its Speed for the purpose of calculating the party's travel speed, your party's travel speed doesn't decrease in difficult terrain, and greater difficult terrain halves your party's travel speed instead of reducing it to a third.

This doesn't increase your party's Speed during an encounter or allow your party to ignore difficult terrain during an encounter.

**Source:** `= this.source` (`= this.source-type`)
