---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Manipulate]]"]
cast: "1 to 3"
range: "varies"
targets: "1 creature"
duration: "1 minute (sustained)"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You draw on nearby spiritual energy or on echoes of the spirits you've invoked throughout your life to temporarily ward living flesh against dangerous spirits. You grant the target a +1 status bonus to saving throws against spells and effects caused by creatures that have the spirit trait and haunts. The number of actions you spend when Casting this Spell determines its targets, range, area, and other parameters.

`pf2:1` The spell has a range of touch.

`pf2:2` (concentrate) The spell has a range of 30 feet. If you target a living creature, the bonus increases to +2.

`pf2:3` (concentrate) You create a ward in a @Template[type:emanation|distance:30]. This targets you and all your allies in the burst.

> [!danger] Effect: Spell Effect: Spirit Ward

**Source:** `= this.source` (`= this.source-type`)
