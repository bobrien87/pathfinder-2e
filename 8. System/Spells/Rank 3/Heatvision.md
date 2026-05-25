---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Fire]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 willing creature"
duration: "1 hour"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The target visually senses the heat energy emitted by the creatures and objects around it, gaining infrared vision at a range of 60 feet as a precise sense. This vision can detect any warm-blooded creature or source of heat not completely covered behind a solid object, such as a wall; this bypasses any concealment granted by smoke or darkness. It can similarly detect especially cold creatures and sources of cold. Almost all creatures with the cold or fire trait can be detected with heatvision. Undead and constructs are typically the same temperature as their environment and can't be detected with heatvision. The GM decides in other cases.

**Heightened (6th)** The duration lasts until you next make your daily preparations, and the range increases to 120 feet.

**Source:** `= this.source` (`= this.source-type`)
