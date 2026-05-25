---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Aftermath]]", "[[Divine]]"]
prerequisites: "You've partied extensively with an azata or entered a romantic relationship with an azata"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You've been ensnared by an azata's infectious enthusiasm for life, love, and freedom that manifests as a pearlescent afterimage in your graceful movements, a spring in your soft steps, an ever-present melody in your euphonic voice, and eddies of passionate colors in your mesmerizing eyes. You gain a +1 circumstance bonus to checks to `act make-an-impression`, or a +2 circumstance bonus if the target is holy. You gain the [[Set Free]] reaction.

**Source:** `= this.source` (`= this.source-type`)
