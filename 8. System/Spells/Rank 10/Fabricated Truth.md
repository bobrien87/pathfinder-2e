---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "10"
traits: ["[[Concentrate]]", "[[Incapacitation]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:3`"
range: "100 feet"
targets: "up to 5 creatures"
defense: "Will"
duration: "varies"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Choose a single statement you want the targets to believe. The fact could be narrow, such as "a dragon is circling overhead and wants to kill me"; wide-reaching, such as "all humanoids are disguised abominations"; or conceptual, such as "if I don't live a kinder life, I'll be punished in the afterlife." The targets' experiences color how they react to this "truth" and how their behavior changes. If the statement changes what they perceive, they treat the change as a sudden revelation. The effect of the spell depends on the targets' Will saves. If a target is already affected by fabricated truth, your spell tries to counteract it. If the counteract check fails, the outcome of the target's saving throw can't be worse than a success.
- **Critical Success** The target doesn't believe the statement, and it knows you tried to trick it.
- **Success** The target doesn't believe the statement or realize you tried to trick it.
- **Failure** The target believes the statement for 1 week.
- **Critical Failure** The target believes the statement with unlimited duration.

**Source:** `= this.source` (`= this.source-type`)
