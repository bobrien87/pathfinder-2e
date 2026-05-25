---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "10"
traits: ["[[Concentrate]]", "[[Healing]]", "[[Manipulate]]", "[[Vitality]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "dead creatures and living creatures of your choice within range"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A burst of healing energy soothes living creatures and temporarily rouses those recently slain. All living targets regain 10d8+40 Hit Points.

In addition, you return any number of dead targets to life temporarily, with the same effects and limitations as [[Raise Dead]]. The raised creatures have a number of temporary Hit Points equal to the Hit Points you gave living creatures, but no normal Hit Points. The raised creatures can't regain Hit Points or gain temporary Hit Points in other ways, and once *revival*'s duration ends, they lose all temporary Hit Points and die.

*Revival* can't resurrect creatures killed by [[Disintegrate]] or a death effect. It has no effect on undead.

**Source:** `= this.source` (`= this.source-type`)
