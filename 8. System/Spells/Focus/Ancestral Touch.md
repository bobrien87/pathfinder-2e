---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Emotion]]", "[[Fear]]", "[[Focus]]", "[[Manipulate]]", "[[Mental]]", "[[Oracle]]"]
cast: "`pf2:1`"
range: "touch"
targets: "1 living creature"
defense: "Will"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You touch a creature and force them to see and feel the ancestors surrounding you. The target takes 2d4 mental damage, with results depending on a Will save.
- **Critical Success** The target is unaffected.
- **Success** The target takes half damage.
- **Failure** The target is [[Frightened]] 1 and takes full damage.
- **Critical Failure** The target is [[Frightened]] 2 and takes double damage.

**Heightened (+1)** The mental damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
