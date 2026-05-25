---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Thaumaturge]]", "[[Witch]]"]
prerequisites: "Enhanced Familiar"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Thaumaturge** By taking the best parts of each magical tradition, you've found a way to grant your familiar even more abilities than other familiars.

**Witch** Your familiar is imbued with even more magic than other familiars.

You can select a base of six familiar or master abilities each day, instead of four.

**Special** Add the bonus familiar abilities you gain for being a witch to this amount.

**Source:** `= this.source` (`= this.source-type`)
