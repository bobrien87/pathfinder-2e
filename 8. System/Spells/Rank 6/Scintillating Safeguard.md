---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Manipulate]]"]
cast: "`pf2:r`"
range: "30 feet"
targets: "up to 5 willing creatures who would be harmed by the triggering effect"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** An effect would deal physical or energy damage to you or a creature in range.

A sparkling magical barrier envelops each target, shielding them against the triggering effect. Choose one type of physical or energy damage the triggering effect deals. Each target gains resistance 10 against that damage type for the triggering effect. The resistance applies only against the initial damage, not against any persistent damage or other lingering effects.

**Heightened (+1)** The resistance increases by 1.

> [!danger] Effect: Spell Effect: Scintillating Safeguard

**Source:** `= this.source` (`= this.source-type`)
