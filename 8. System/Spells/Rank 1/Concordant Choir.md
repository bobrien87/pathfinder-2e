---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Sonic]]"]
cast: "1 to 3"
range: "30 feet"
targets: "varies"
defense: "basic Fortitude"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You unleash a dangerous consonance of reverberating sound, focusing on a single target or spreading out to damage many foes. The number of actions you spend Casting this Spell determines its targets, range, area, and other parameters.

`pf2:1` The spell deals 1d4 sonic damage to a single enemy, with a basic Fortitude save.

`pf2:2` (manipulate) The spell deals 2d4 sonic damage to all creatures in a @Template[burst|distance:10], with a basic Fortitude save.

`pf2:3` (manipulate) The spell deals 2d4 sonic damage to all creatures in a @Template[emanation|distance:30], with a basic Fortitude save.

**Heightened (+1)** The damage increases by 1d4 for the 1-action version, or 2d4 for the other versions.

**Source:** `= this.source` (`= this.source-type`)
