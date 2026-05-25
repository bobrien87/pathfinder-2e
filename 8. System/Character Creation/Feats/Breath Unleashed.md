---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Kobold]]"]
prerequisites: "Kobold Breath"
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You're able to channel more of your draconic benefactor's power and focus it into your [[Kobold Breath]], increasing its effectiveness but requiring more time to recover. When you use Kobold Breath, you can increase the damage dice to d8s and increase the area to @Template[cone|distance:30]{30 feet for a cone} or @Template[line|distance:60]{60 feet for a line}. If you do, you can't use Kobold Breath again for 1 hour. During this time, Kobold Breath cannot be recharged using Kobold Momentum.

**Source:** `= this.source` (`= this.source-type`)
