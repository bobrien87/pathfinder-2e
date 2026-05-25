---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Bard]]", "[[Composition]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "you or 1 ally"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your symphony lifts listeners from their worldly concerns. Attempt a Performance check to counteract an effect applying one of the following conditions to the target: [[Grabbed]], [[Immobilized]], [[Paralyzed]], [[Restrained]], [[Slowed]], or [[Stunned]]. If you fail, you can't target the same effect on the target for 1 day. Use the condition's source to determine the counteract DC (for example, the [[Escape]] DC for grabbed).

**Heightened (9th)** You can target up to four creatures.

**Source:** `= this.source` (`= this.source-type`)
