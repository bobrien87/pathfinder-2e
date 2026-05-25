---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Force]]", "[[Manipulate]]"]
cast: "`pf2:2`"
duration: "8 hours"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A small platform of magical force materializes adjacent to you to carry cargo. It is [[Invisible]] or has a ghostly appearance, is 2 feet in diameter, and follows 5 feet behind you, floating just above the ground. It holds up to 5 Bulk of objects (if they can fit on it). Any objects atop the platform fall to the ground when the spell ends. You can Sustain the spell to move the platform up to 30 feet along the ground, to make it stay in place, or to have it return to you and resume following you. The spell ends if a creature tries to ride atop the platform, if the platform is overloaded, if anyone tries to lift or force the platform higher above the ground, or if you move more than 60 feet away from the platform.

**Heightened (4th)** The platform can carry 10 Bulk, creatures can ride atop it, and it can hover in the air, not just on the ground

**Source:** `= this.source` (`= this.source-type`)
