---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Rogue]]"]
prerequisites: "trained in Deception"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You goad a foe into overextending. On a successful [[Feint]], you can use the following success and critical success effects instead of any other effects that would occur when you Feint.
- **Critical Success** The target takes a –2 circumstance penalty to all attack rolls against you before the end of its next turn.
- **Success** The target takes a –2 circumstance penalty to its next attack roll against you before the end of its next turn.

**Source:** `= this.source` (`= this.source-type`)
