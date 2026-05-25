---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ""
traditions: ""
cast: ""
range: ""
area: ""
targets: ""
defense: ""
duration: ""
trigger: ""
requirements: ""
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traits != null, "<br>**Traits** " + this.traits, "") + choice(this.traditions != null, "<br>**Traditions** " + this.traditions, "")`

`= "**Cast** " + this.cast + choice(this.trigger != null, "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null, "<br>**Requirements** " + this.requirements, "") + choice(this.range != null or this.area != null or this.targets != null, "<br>" + choice(this.range != null, "**Range** " + this.range, "") + choice(this.area != null, choice(this.range != null, "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null, choice(this.range != null or this.area != null, "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null or this.duration != null, "<br>" + choice(this.defense != null, "**Defense** " + this.defense, "") + choice(this.duration != null, choice(this.defense != null, "; ", "") + "**Duration** " + this.duration, ""), "")`

You exhale deadly magical energy in an area, dealing @Damage[10d6[untyped]|options:area-damage] damage to each creature in the area with a basic save against your spell DC. The shape, damage type, and save type match that of your chosen dragon's breath. If the chosen dragon's breath can deal more than one type of damage, choose one when you cast *dragon form*. The shape is a @Template[type:cone|distance:30] or a @Template[type:line|distance:100]. Once activated, Dragon Breath can't be used again for 1d4 rounds. Dragon Breath has the tradition trait matching the type of dragon and the damage trait matching the type of damage it deals, if applicable.

**Source:** `= this.source` (`= this.source-type`)
