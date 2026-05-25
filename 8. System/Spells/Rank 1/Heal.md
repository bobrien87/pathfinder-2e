---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Healing]]", "[[Manipulate]]", "[[Vitality]]"]
cast: "1 to 3"
range: "varies"
targets: "1 willing living creature or 1 undead"
defense: "basic Fortitude"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You channel vital energy to heal the living or damage the undead. If the target is a willing living creature, you restore 1d8 Hit Points. If the target is undead, you deal that amount of vitality damage to it, and it gets a basic Fortitude save. The number of actions you spend when Casting this Spell determines its targets, range, area, and other parameters.

`pf2:1` The spell has a range of touch.

`pf2:2` (concentrate) The spell has a range of 30 feet. If you're healing a living creature, increase the Hit Points restored by 8.

`pf2:3` (concentrate) You disperse vital energy in a @Template[emanation|distance:30]. This targets all living and undead creatures in the burst.

**Heightened (+1)** The amount of healing or damage increases by 1d8, and the extra healing for the 2-action version increases by 8.

**Source:** `= this.source` (`= this.source-type`)
