---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Attack]]", "[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "120 feet"
targets: "1 creature, unattended object, or force construct"
defense: "basic Fortitude"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A black tracer bolt flies toward your target, and upon making contact intensifies into a powerful destructive beam. Make a spell attack against the target. If you hit an object or force construct (such as a wall of force), it's destroyed with no save unless it's an artifact or similarly powerful. A single casting can destroy no more than a 10-foot cube of matter. If you hit a creature, it takes 12d10 damage (no damage type) with a basic Fortitude save. If you critically hit, the target gets a result one degree of success worse than the outcome of its Fortitude save. A creature reduced to 0 HP is blasted to fine powder; its gear remains.

**Heightened (+1)** The damage increases by 2d10.

**Source:** `= this.source` (`= this.source-type`)
