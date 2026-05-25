---
type: action
source-type: "Remaster"
cast: "`pf2:r`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Trigger** A creature within 30 feet Casts a Spell or Activates an Item using a concentrate Activation

**Effect** You set off a firework that explodes with a loud screech near the creature. The creature must attempt a [[Will]] save.
- **Success** The creature is unaffected.
- **Failure** The creature must use an additional action on the triggering action or activity, or it's disrupted.
- **Critical Failure** The triggering action is disrupted.

**Source:** `= this.source` (`= this.source-type`)
