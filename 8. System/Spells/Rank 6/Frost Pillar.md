---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Cold]]", "[[Concentrate]]", "[[Manipulate]]", "[[Water]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Reflex"
duration: "1 minute (sustained)"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Ice crystallizes around a creature, imprisoning it within an icy pillar. On a successful saving throw, the creature is pushed to an adjacent space of its choice; otherwise, it's frozen inside the pillar and becomes [[Restrained]] as its body can barely move within the ice. The ice has AC 10, Hardness 10, and 60 Hit Points; it's immune to critical hits, cold damage, and precision damage, and it has weakness 15 to fire. If the ice is destroyed, the creature within is freed and the spell immediately ends.

**Source:** `= this.source` (`= this.source-type`)
