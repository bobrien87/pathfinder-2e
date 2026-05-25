---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Illusion]]", "[[Manipulate]]", "[[Subtle]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 creature"
duration: "10 minutes"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Illusions bend light around the target, rendering it [[Invisible]]. This makes it [[Undetected]] to all creatures, though the creatures can attempt to find the target, making it [[Hidden]] to them instead. If the target uses a hostile action, the spell ends after that hostile action is completed.

**Heightened (4th)** The spell lasts 1 minute, but it doesn't end if the target uses a hostile action.

**Source:** `= this.source` (`= this.source-type`)
