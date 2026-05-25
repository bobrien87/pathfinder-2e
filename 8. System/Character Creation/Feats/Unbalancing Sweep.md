---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Barbarian]]", "[[Flourish]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You make a great sweep with your weapon or fists about yourself, knocking creatures off their feet and away from you. Choose up to three enemies within your reach and choose whether to [[Shove]] or [[Trip]] all three of them. Whichever of the two options you choose, roll a separate Athletics check against each enemy, performing the same action against each enemy. Each attempt counts toward your multiple attack penalty, but don't increase your penalty until you have made all the attempts.

**Source:** `= this.source` (`= this.source-type`)
