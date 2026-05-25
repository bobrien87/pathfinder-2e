---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Fire]]", "[[Focus]]", "[[Light]]", "[[Manipulate]]", "[[Oracle]]"]
cast: "`pf2:2`"
area: "15-foot cone"
defense: "Reflex"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You fling a spray of tiny shooting stars, dealing 2d4 fire damage. Each creature in the area must attempt a Reflex save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage and is [[Dazzled]] for 1 round.
- **Failure** The creature takes full damage and is dazzled for 3 rounds.
- **Critical Failure** The creature takes double damage and is dazzled for 1 minute.

**Heightened (+1)** Increase the damage by 1d4.

**Source:** `= this.source` (`= this.source-type`)
