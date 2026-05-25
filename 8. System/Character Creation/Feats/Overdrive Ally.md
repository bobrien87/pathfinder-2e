---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Inventor]]", "[[Manipulate]]"]
prerequisites: "Overdrive"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are currently in overdrive.

You quickly fling some of your powered-up mechanisms to an ally, sharing your benefits with them briefly. Choose an ally within 30 feet. Until the end of their next turn, that ally's Strikes deal additional damage equal to half your Intelligence modifier, or your full Intelligence modifier if you were in critical overdrive. The ally doesn't gain the increased damage from expert, master, or legendary overdrive.

> [!danger] Effect: Overdrive Ally

**Source:** `= this.source` (`= this.source-type`)
