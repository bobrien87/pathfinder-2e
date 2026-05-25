---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Metal]]"]
cast: "`pf2:3`"
range: "120 feet"
area: "20-foot burst"
defense: "basic Fortitude"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Red-blown flecks of rust jitter in the air, forming a cloud of agitated particles. All creatures within the cloud become [[Concealed]], and all creatures outside the cloud become concealed to creatures within it. The cloud deals 5d10 slashing damage to any creature that starts its turn in the area, with a basic Fortitude save.

Metal that rusts off of a creature adds to the cloud. When a metal creature takes damage from the cloud, the cloud's area increases by 5 feet (to a maximum of a @Template[burst|distance:40]), and the creature starts to rust, taking @Damage[(floor(@item.level/2)-1)d4[persistent,slashing]] damage. You can Dismiss the cloud.

**Heightened (+2)** The cloud's slashing damage increases by 1d10 and the persistent damage increases by 1d4.

**Source:** `= this.source` (`= this.source-type`)
