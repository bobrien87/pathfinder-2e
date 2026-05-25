---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Cold]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Oracle]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "basic Fortitude"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call upon the frigid depths of outer space to bring a terrible chill to your enemy. The target is cloaked in the freezing void, which deals 3d6 cold damage immediately and the first time each round you Sustain the Spell on future turns, with a basic Fortitude save.

The target is [[Fatigued]] for as long as the effect persists.

**Heightened (+1)** The cold damage increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
