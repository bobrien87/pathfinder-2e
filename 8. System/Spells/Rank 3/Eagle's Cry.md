---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Manipulate]]", "[[Sonic]]"]
cast: "`pf2:2`"
area: "30-foot cone"
defense: "Fortitude"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You let out the mighty cry of a majestic eagle that pierces eardrums. This cry deals 4d8 sonic damage. Each creature in the area must attempt a Fortitude saving throw.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage and is [[Frightened]] 1.
- **Failure** The creature takes full damage and is [[Frightened]] 2.
- **Critical Failure** The creature takes double damage, is frightened 2, and is [[Fleeing]] for 1 round.

**Heightened (+2)** The damage increases by 3d8.

**Source:** `= this.source` (`= this.source-type`)
