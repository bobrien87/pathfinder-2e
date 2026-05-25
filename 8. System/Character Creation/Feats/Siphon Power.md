---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Witch]]"]
frequency: "once per day"
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

**Requirements** You haven't acted yet on your turn.

You draw upon the reservoir of your patron's magic that resides within your familiar. During your turn, you can cast one spell your familiar knows that was granted by your patron or lessons without spending a spell slot to do so (or even having it prepared). The spell must be at least 1 rank lower than your highest-rank witch spell slot.

**Special** This feat has the trait corresponding to the tradition of spells you cast (arcane, divine, occult, or primal).

**Source:** `= this.source` (`= this.source-type`)
