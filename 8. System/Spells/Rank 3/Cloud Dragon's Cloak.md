---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Air]]", "[[Manipulate]]"]
cast: "`pf2:r`"
range: "60 feet"
targets: "the creature targeted by the attack"
duration: "1 round"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** You or an ally in range is targeted by a ranged attack.

A cloud of mist enshrouds the target, appearing much like the deflecting clouds created by cloud dragons. The target is treated as [[Hidden]] for the purposes of resolving the triggering attack (so normally the attacker must succeed at a DC 11 flat check to target it) and all ranged attacks against it for the duration.

**Source:** `= this.source` (`= this.source-type`)
