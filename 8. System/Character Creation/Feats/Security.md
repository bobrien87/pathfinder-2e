---
type: feat
source-type: "Remaster"
level: "4"
traits: ["[[Champion]]"]
prerequisites: "shields of the spirit"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Those you shield can benefit from your lasting protection. You can cast [[Shields of the Spirit]] using 2 actions instead of 1. If you do, you can choose one ally in your champion's aura to gain a spirit shield that accompanies it. For 1 minute, that ally gains the benefits of *shields of the spirit*, even while the ally isn't in your champion's aura and even if your shield isn't raised. If you create another companion shield, any previous one ends.

**Source:** `= this.source` (`= this.source-type`)
