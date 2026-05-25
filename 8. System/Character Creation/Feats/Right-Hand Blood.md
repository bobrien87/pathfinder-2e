---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Kholo]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

It's said that the flesh of the right side of a hyena can heal diseases, but that the flesh of the left side is deadly and poisonous. You can deal 1 slashing damage to yourself to feed someone blood from your right side and Administer First Aid or take 2d8 untyped damage to [[Treat Disease]] or [[Treat Wounds]]; in either case, you don't need a healer's toolkit, and you gain a +1 item bonus to your check. Blood from your left side causes the check to critically fail automatically.

**Source:** `= this.source` (`= this.source-type`)
