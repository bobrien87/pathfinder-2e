---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Fighter]]", "[[Press]]"]
source: "Pathfinder Player Core"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You have a creature [[Grabbed]].

You pummel a held foe, hoping to stagger them. Make a melee Strike against a creature you have grabbed. The weapon damage from this Strike is bludgeoning damage. If the Strike hits, the creature must attempt a [[Fortitude]] save against your class DC; this is an incapacitation effect.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Stunned]] 1.
- **Failure** The creature is [[Stunned]] 2.
- **Critical Failure** The creature is [[Stunned]] 3.

**Source:** `= this.source` (`= this.source-type`)
