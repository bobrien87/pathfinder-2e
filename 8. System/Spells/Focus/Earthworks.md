---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Earth]]", "[[Focus]]", "[[Manipulate]]", "[[Wizard]]"]
cast: "1 to 3"
range: "60 feet"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

With a ripple of earth, you raise small barriers from the ground. The ground in the area becomes difficult terrain. The spell's area is a @Template[burst|distance:5] if you spent 1 action to cast it, a @Template[burst|distance:10] if you spent 2 actions, or a @Template[burst|distance:15] if you spent 3 actions. A creature can Interact to clear the barriers from one 5-foot square adjacent to it.

**Heightened (4th)** You pull the barriers to float in the air, causing the spell to function as difficult terrain for flying creatures

**Source:** `= this.source` (`= this.source-type`)
