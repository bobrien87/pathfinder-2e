---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Focus]]", "[[Hex]]", "[[Manipulate]]", "[[Witch]]"]
cast: "`pf2:r`"
range: "60 feet"
targets: "your familiar"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** Your familiar would take damage.

Your patron momentarily recalls your familiar to the ether, shifting it from its solid, physical form into a ghostly version of itself. Against the triggering damage, your familiar gains resistance 5 to all damage and is immune to precision damage.

> [!danger] Effect: Spell Effect: Phase Familiar

**Heightened (+1)** Increase the resistance by 2.

**Source:** `= this.source` (`= this.source-type`)
