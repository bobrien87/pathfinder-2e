---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Focus]]", "[[Healing]]", "[[Ranger]]", "[[Vitality]]"]
cast: "1 or 2"
range: "touch or 30 feet"
targets: "your animal companion"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You heal your animal companion's wounds. You restore 1d10 Hit Points to your animal companion. The number of actions you spend Casting this Spell determines range and other parameters.

`pf2:1` (manipulate) The spell has a range of touch.

`pf2:2` (concentrate, manipulate) The spell has a range of 30 feet and restores an additional 8 Hit Points to the target.

**Heightened (+1)** The amount of healing increases by 1d10, and the additional healing for the 2-action version increases by 8.

**Source:** `= this.source` (`= this.source-type`)
