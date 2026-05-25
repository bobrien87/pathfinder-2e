---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Linguistic]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "until the end of the target's next turn"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You shout a command that's hard to ignore. You can command the target to approach you, run away (as if it had the [[Fleeing]] condition), release what it's holding, drop [[Prone]], or stand in place. It can't [[Delay]] or take any reactions until it has obeyed your command. The effects depend on the target's Will save.
- **Success** The creature is unaffected.
- **Failure** For the first action on its next turn, the creature must use a single action to do as you command.
- **Critical Failure** The target must use all its actions on its next turn to obey your command.

**Heightened (5th)** You can target up to 10 creatures.

**Source:** `= this.source` (`= this.source-type`)
