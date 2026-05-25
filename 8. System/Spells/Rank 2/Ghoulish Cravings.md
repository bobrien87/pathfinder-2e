---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Curse]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 creature"
defense: "Will"
duration: "varies"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You touch the target to afflict it with the overwhelming desire to eat raw meat. The target must attempt a Will save.
- **Critical Success** The target is unaffected.
- **Success** The target is [[Sickened]] 1 by its unbidden hunger.
- **Failure** The target is [[Sickened]] 2 and can't reduce this condition below sickened 1 until it first consumes some raw meat; if the creature doesn't have access to raw meat, it can take a bite out of a corpse within reach as an Interact action.
- **Critical Failure** As failure, but the target can't reduce the condition below sickened 2 until it consumes raw meat.

**Source:** `= this.source` (`= this.source-type`)
