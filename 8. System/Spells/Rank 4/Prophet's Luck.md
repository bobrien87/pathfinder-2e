---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:r`"
range: "60 feet"
targets: "1 creature"
duration: "10 minutes"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** You or a creature within range attempts a saving throw against an obvious threat.

You prophesize the result of the triggering saving throw as either a success (including a critical success) or a failure (including a critical failure). The target gains a +1 status bonus to the save if you predict success or a –1 status penalty if you predict failure. If you predict the result correctly, fortune favors you, and you gain a +1 status bonus to saving throws. If you predict incorrectly, fortune spurns the target, imparting a –1 status penalty to its saving throws.

**Heightened (6th)** The save bonus or penalty increases to +2 or –2.

**Heightened (9th)** The save bonus or penalty increases to +3 or –3.

**Source:** `= this.source` (`= this.source-type`)
