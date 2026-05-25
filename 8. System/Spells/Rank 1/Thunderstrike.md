---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Electricity]]", "[[Manipulate]]", "[[Sonic]]"]
cast: "`pf2:2`"
range: "120 feet"
targets: "1 creature"
defense: "basic Reflex"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call down a tendril of lightning that cracks with thunder, dealing 1d12 electricity damage and 1d4 sonic damage to the target with a basic Reflex save. A target wearing metal armor or made of metal takes a –1 circumstance bonus to its save, and if damaged by the spell is [[Clumsy]] 1 for 1 round.

**Heightened (+1)** The damage increases by 1d12 electricity and 1d4 sonic.

**Source:** `= this.source` (`= this.source-type`)
