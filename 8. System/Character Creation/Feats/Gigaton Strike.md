---
type: feat
source-type: "Remaster"
level: "8"
traits: ["[[Inventor]]"]
prerequisites: "Megaton Strike"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

When you use a full-power Megaton Strike, you can knock your foe back. When you succeed at your Strike while using an unstable Megaton Strike, your target must attempt a [[Fortitude]] save against your class DC.
- **Critical Success** The creature is unaffected.
- **Success** The creature is pushed back 5 feet.
- **Failure** The creature is pushed back 10 feet.
- **Critical Failure** The creature is pushed back 20 feet.

**Special** If your innovation is a minion, this benefit applies on its unstable Megaton Strikes.

**Source:** `= this.source` (`= this.source-type`)
