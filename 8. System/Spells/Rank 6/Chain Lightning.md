---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Electricity]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "500 feet"
targets: "1 creature, plus any number of additional creatures"
defense: "basic Reflex"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You discharge a powerful bolt of lightning at the target, dealing 8d12 electricity damage. The target must attempt a basic Reflex save. The electricity arcs to another creature within 30 feet of the first target, jumps to another creature within 30 feet of that target, and so on. You can end the chain at any point. You can't target the same creature more than once, and you must have line of effect to all targets. Roll the damage only once, and apply it to each target (halving or doubling as appropriate for its saving throw outcome). The chain ends if any one of the targets critically succeeds at its save.

**Heightened (+1)** The damage increases by 1d12.

**Source:** `= this.source` (`= this.source-type`)
