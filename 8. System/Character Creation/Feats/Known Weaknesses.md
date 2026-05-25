---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Investigator]]"]
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Whenever you [[Devise a Stratagem]], you can also attempt a check to [[Recall Knowledge]] as part of that action before rolling the d20. If you critically succeed at the Recall Knowledge check, you notice a weakness and can convey the information to allies to grant each of them a +1 circumstance bonus to their next attack roll against the subject, as long as their attack is made before the beginning of your next turn. If you choose an attack stratagem, this bonus applies to that attack roll too.

> [!danger] Effect: Known Weaknesses

**Source:** `= this.source` (`= this.source-type`)
