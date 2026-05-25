---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Kobold]]"]
source: "Pathfinder Lost Omens Draconic Codex"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You possess features that dragons find particularly cute or charming, making it easier to endear yourself to them, or at least cause them to momentarily forgive your insolence. You gain a +2 circumstance bonus to Perception checks and saving throws against dragons. In addition, whenever you meet a creature with the dragon trait in a social situation, you can attempt a Diplomacy check to `act make-an-impression` on that creature immediately, rather than after conversing for 1 minute; you take a –5 circumstance penalty to this check. If you fail, you can choose to engage in 1 minute of conversation and then attempt a new check rather than accept the failure or critical failure result.

**Source:** `= this.source` (`= this.source-type`)
