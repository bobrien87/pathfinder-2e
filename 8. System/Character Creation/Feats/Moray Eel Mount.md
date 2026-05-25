---
type: feat
source-type: "Remaster"
level: "9"
traits: ["[[Athamaru]]"]
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You have either trained a giant moray eel since its hatching or have tamed one in the wild. You gain the [[Bonded Animal]] skill feat, even if you don't meet the prerequisites, to bond with a giant moray eel. When you [[Command this Animal]] while you are mounted on it to take a move action, you automatically succeed instead of needing to attempt a check.

**Special** If you have the Elver Pet or Growing Eel Friend ancestry feats, you can choose to have that pet become your bonded animal. You don't need to spend 7 days of downtime to bond with the eel, and you automatically succeed at the Nature check. You can then retrain those feats.

**Source:** `= this.source` (`= this.source-type`)
