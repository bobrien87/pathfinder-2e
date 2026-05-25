---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Cold]]", "[[Concentrate]]", "[[Manipulate]]", "[[Water]]"]
cast: "`pf2:3`"
range: "120 feet"
area: "20-foot burst"
defense: "Reflex"
duration: "10 minutes (sustained)"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Intense cold rain comes from nowhere, a microcosm of a sudden downpour, and a magical tweak can turn the rain to freezing sleet. The driving rain and pooling water make the area difficult terrain and extinguish non-magical fires.

On subsequent rounds, the first time you Sustain the spell each round, you can move the area up to 20 feet and can also freeze the rain. If you freeze the rain, each creature in the area takes 4d6 cold damage and might be slowed, depending on result of its Reflex save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage and is [[Slowed]] 1 for 1 round.
- **Critical Failure** The creature takes double damage and is [[Slowed]] 2 for 1 round.

**Heightened (+1)** The damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
