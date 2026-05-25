---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "7"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Monk]]"]
cast: "`pf2:2`"
area: "30-foot emanation"
defense: "Fortitude"
requirements: "You are in clinging shadow stance."
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Grasping darkness surges from you, dealing 14d4 void damage. Each creature in the area must attempt a Fortitude save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage and is [[Enfeebled]] 1 for 1 round.
- **Failure** The creature takes full damage and is [[Enfeebled]] 2 for 1 round.
- **Critical Failure** The creature takes double damage, is [[Stunned]] 1, and enfeebled 2 for 1 round, and [[Immobilized]] for 1 round or until it Escapes, whichever comes first.

**Heightened (+1)** The void damage increases by 2d4.

**Source:** `= this.source` (`= this.source-type`)
