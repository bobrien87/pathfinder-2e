---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Attack]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Ranger]]", "[[Sonic]]"]
cast: "`pf2:2`"
area: "15-foot cone"
targets: "1 creature within reach"
defense: "basic Fortitude"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Imitating raptorial creatures, you attack with such speed it drives a sonic shockwave. Make a melee Strike against a creature in your reach; if you hit, you deal an additional 3d8 sonic damage. Regardless of the result of your Strike, that creature becomes the point of origin of a 15-foot cone, aimed directly away from you. All creatures in that cone take 6d8 sonic damage (basic Fortitude save).

**Heightened (+1)** The damage of the cone increases by 1d8.

**Source:** `= this.source` (`= this.source-type`)
