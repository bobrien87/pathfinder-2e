---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Attack]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Sorcerer]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "2 creatures no more than 10 feet from each other"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Vicious dragon claws appear and slash at two nearby foes. Make a spell attack roll against each creature. This counts as two attacks for your multiple attack penalty, but the penalty doesn't increase until you've made both attacks. On a hit, the creatures takes 1d8 slashing plus 1d4 additional damage of a type determined by the magical tradition related to the dragon that influenced your bloodline: **arcane** force, **divine** spirit, **occult** mental, or **primal** fire.

**Heightened (+1)** The initial damage increases by 1d8 and the additional damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
