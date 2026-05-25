---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Earth]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "60 feet"
area: "10-foot burst"
defense: "Fortitude"
duration: "1 minute (sustained)"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Handlike protrusions of rock and soil grab and bury creatures. Each creature in the area when you cast the spell, and each creature that ends its turn in the area during the spell's duration, must attempt a Fortitude save. The first time each round you Sustain this spell, each creature still [[Grabbed]] by the earth takes 1d6 bludgeoning damage, and each creature [[Restrained]] by the earth takes 2d6 bludgeoning damage. A creature can attempt to [[Escape]], rolling against your spell DC.
- **Success** The creature is unaffected.
- **Failure** The creature is grabbed by the earth.
- **Critical Failure** The creature is restrained by the earth.

**Heightened (+2)** The bludgeoning damage dealt when you Sustain this spell increases by 1d6 for grabbed creatures and 2d6 for restrained creatures.

**Source:** `= this.source` (`= this.source-type`)
