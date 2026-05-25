---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Druid]]"]
prerequisites: "leaf order"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You call a minor spirit of nature into a plant body, creating a leshy companion to aid you in your spellcasting. You gain a familiar, which has your choice of either the plant or fungus familiar ability; this doesn't count against your usual limit of familiar abilities (typically 2). The spirit you call has a more tenuous connection to its plant body than fully independent leshies, so it is Tiny in size like other familiars.

**Source:** `= this.source` (`= this.source-type`)
