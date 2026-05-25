---
type: feat
source-type: "Remaster"
level: "5"
traits: ["[[Kobold]]"]
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You're a cunning adversary in close quarters and are well-versed in hit-and-run tactics that exploit the advantages of your small stature. As part of your training, you learned what to do when you're [[Grabbed]] or [[Restrained]]. You gain a +1 circumstance bonus to checks to Escape, and after resolving a successful Escape action, you can immediately use your reaction to Step or to `act shove` or `act trip` the creature from whom you just Escaped.

**Source:** `= this.source` (`= this.source-type`)
