---
type: action
source-type: "Remaster"
traits: ["[[Finisher]]"]
cast: "`pf2:1`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

You make an incredibly graceful attack, piercing your foe's defenses. Make a Strike with the following failure effect.
- **Failure** You deal half your [[Precise Strike]] damage to the target. This damage type is that of the weapon or unarmed attack you used for the Strike.

**Source:** `= this.source` (`= this.source-type`)
