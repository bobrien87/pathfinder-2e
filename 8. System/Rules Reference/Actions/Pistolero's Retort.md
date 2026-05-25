---
type: action
source-type: "Remaster"
traits: ["[[Gunslinger]]"]
cast: "`pf2:r`"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** You're wielding a one-handed firearm or one-handed crossbow.

**Trigger** A foe within the first range increment of the one-handed firearm or one-handed crossbow you're wielding critically fails an attack roll against you.

You punish your foe's failure with a shot. Make a Strike against the triggering foe with a one-handed firearm or one-handed crossbow.

**Source:** `= this.source` (`= this.source-type`)
