---
type: action
source-type: "Remaster"
traits: ["[[Attack]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You attack with a weapon you're wielding or with an unarmed attack, targeting one creature within your reach (for a melee attack) or within range (for a ranged attack). Roll an attack roll using the attack modifier for the weapon or unarmed attack you're using, and compare the result to the target creature's AC to determine the effect.
- **Critical Success** You make a damage roll according to the weapon or unarmed attack and deal double damage.
- **Success** You make a damage roll according to the weapon or unarmed attack and deal damage.

**Source:** `= this.source` (`= this.source-type`)
