---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Light]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "120 feet"
area: "10-foot burst"
defense: "Reflex"
duration: "varies"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A wave of magical light washes over the area. You choose the appearance of the light, such as colorful, heatless flames or sparkling motes. A creature affected by *revealing light* is [[Dazzled]]. If the creature was [[Invisible]], it becomes [[Concealed]] instead. If the creature was already concealed for any other reason, it is no longer concealed.
- **Critical Success** The target is unaffected.
- **Success** The light affects the creature for 2 rounds.
- **Failure** The light affects the creature for 1 minute.
- **Critical Failure** The light affects the creature for 10 minutes.

**Source:** `= this.source` (`= this.source-type`)
