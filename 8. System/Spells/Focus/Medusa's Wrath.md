---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "8"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Monk]]"]
cast: "`pf2:2`"
defense: "Fortitude"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You make an attack filled with a medusa's petrifying power. Make an unarmed Strike with the following additional effects.
- **Critical Success** The target is [[Slowed]] 2 and must attempt a Fortitude save at the end of each of its turns; this ongoing save has the incapacitation trait. On a failed save, the slowed condition increases by 1 (2 on a critical failure). A successful save reduces the slowed condition by 1. When a creature is unable to act due to the slowed condition from medusa's wrath, it is [[Petrified]] permanently. The spell ends if the creature is petrified or the slowed condition is removed.
- **Success** As critical success, but the target is initially [[Slowed]] 1

**Source:** `= this.source` (`= this.source-type`)
